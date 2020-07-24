from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from question.forms import QuestionForm
from django.http import HttpResponse
import os
import logging
from question.models import *
import json

from django.shortcuts import redirect
from django.shortcuts import get_object_or_404

logger = logging.getLogger(__name__)

def  new_question(request):
	context = {}
	if request.method == 'POST' :
		form = QuestionForm(request.POST)	 	
		if form.is_valid(): 
			users_question = form.cleaned_data['question']
			question_tags = form.cleaned_data['tags'].split(',')
			user_email = request.session['user_email'] 
			user = User.objects.get(email=user_email)

			current_question = Question.objects.create(question=users_question,asked_by=user)
			current_question.save()

			for current_tag in question_tags : 
					if not Tag.objects.filter(tag_name=current_tag).exists():
						my_tag =  Tag.objects.create(tag_name=current_tag)
						my_tag.save()
					else :
						my_tag = Tag.objects.get(tag_name=current_tag)
					question_tag_map = 	QuestionTagMap(question=current_question,tag=my_tag)
					question_tag_map.save()
			return redirect(current_question)
	form = QuestionForm()
	context = {
			'form':form,
	}
	return render(request,'question/new_question.html',context)

def question(request,question_id):
	current_question = Question.objects.get(id=question_id)
	user_email = request.session['user_email']
	current_user = User.objects.get(email=user_email)
	context = {}
	context.update({'add_answer_button':'True'})
	if current_question.asked_by.email == request.session['user_email'] :
		context.update({'add_answer_button': 'False'})
	if Answer.objects.filter(question=current_question,answered_by=current_user).exists():
		context.update({'add_answer_button': 'False'})
	context.update({'question': current_question})
	answers = Answer.objects.filter(question__id=question_id)
	option_for_answer = []
	for current_answer in answers:
		if not AnswerUpvoteDownvoteTable.objects.filter(answer=current_answer,user=current_user).exists():
			option_for_answer.append('both')
		else:
			answer_user_action = AnswerUpvoteDownvoteTable.objects.get(answer=current_answer,user=current_user)
			option_for_answer.append(answer_user_action.reaction)
	context.update({'answers':answers })
	context.update({'option_for_answer':option_for_answer})
	return render(request,'question/view_question.html',context)

def add_answer(request,question_id):
	current_question = Question.objects.get(id=question_id)
	user_email = request.session['user_email']
	user = User.objects.get(email=user_email)
	Answer.objects.filter()
	answer_text = request.GET['new_answer_text']
	answer = Answer.objects.create(answer=answer_text,answered_by=user,question=current_question)
	answer.save()
	return redirect(current_question)

def upvote_answer(request,answer_id):
	answer = Answer.objects.get(id=answer_id)
	user_email = request.session['user_email']
	user = User.objects.get(email=user_email)
	user_action = AnswerUpvoteDownvoteTable.objects.create(answer=answer,user=user,reaction="UPVOTE")
	answer.upvotes = answer.upvotes+1
	answer.save()
	user_action.save()
	dict = {'success': "true"}
	return HttpResponse(json.dumps(dict), content_type='application/json')


def downvote_answer(request,answer_id):
	answer = Answer.objects.get(id=answer_id)
	user_email = request.session['user_email']
	user = User.objects.get(email=user_email)
	user_action = AnswerUpvoteDownvoteTable.objects.create(answer=answer, user=user, reaction="DOWNVOTE")
	answer.downvotes = answer.downvotes + 1
	answer.save()
	user_action.save()
	dict = {'success': "true"}
	return HttpResponse(json.dumps(dict), content_type='application/json')





				


