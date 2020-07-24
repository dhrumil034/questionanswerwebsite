from django import forms 



class SignUp(forms.Form):
	username = forms.CharField(max_length=20)
	email = forms.EmailField()
	password = forms.CharField(widget=forms.PasswordInput)
	bio = forms.CharField(widget=forms.Textarea)
	profile_image = forms.ImageField()

class Login(forms.Form):
	email = forms.EmailField() 
	password = forms.CharField(widget=forms.PasswordInput)