from django.shortcuts import render
from user.models import User 
from user.models import Password 
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.db import transaction
from user.forms import SignUp
from user.forms import Login
import hashlib 
import os
import logging 

logger = logging.getLogger(__name__)


def view_bio(request):
	user = User.objects.get(email=request.session['user_email'])
	return render(request,'user/user_bio.html',{'user': user})


def login(request):
	context = {}
	if request.method == 'POST' :
		form = Login(request.POST)
		if form.is_valid():
			user_email = form.cleaned_data['email']
			user_password = form.cleaned_data['password']
			user = User.objects.get(email=user_email) 
			print("inside verfication")
			print(str(user is not None))
			if user is not None and user.verify_password(user_password):
				print('password verfication successful')
				request.session['user_email'] = form.cleaned_data['email']	
				return HttpResponseRedirect(reverse('view_bio'))
			else :
				context.update({'failed_login': 'true'})
	else:
		context.update({'failed_login': 'false'})
		form = Login()
		context.update({'form': form })
	print('rerendering login page')	
	return render(request,'user/login.html',context)	

def signup(request):
	if request.method == 'POST' :
		form = SignUp(request.POST, request.FILES)
		if form.is_valid():
			new_salt = os.urandom(32) 
			hased_key = hashlib.pbkdf2_hmac(
					    'sha256', # The hash digest algorithm for HMAC
					    form.cleaned_data['password'].encode('utf-8'), # Convert the password to bytes
					    new_salt, # Provide the salt
					    100000 # It is recommended to use at least 100,000 iterations of SHA-256 
						)

			password = Password.objects.create(salt=new_salt,key=hased_key)
			password.save()
			user = User.objects.create(name=form.cleaned_data['username'],bio=form.cleaned_data['bio'],email=form.cleaned_data['email'],password=password,profile_image=form.cleaned_data['profile_image'])
			user.save()
			request.session['user_email'] = form.cleaned_data['email'] 
			return HttpResponseRedirect(reverse('view_bio') )

	else : 
		form = SignUp()
		context = {
			'form':form,
		}
		return render(request,'user/signup.html',context)

		




