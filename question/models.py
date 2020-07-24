from django.conf import settings
from django.db import models
from django.utils import timezone 
from user.models import User
from model_utils import Choices
import os



class Question(models.Model):
	question = models.TextField() 
	asked_by = models.ForeignKey(User,on_delete=models.CASCADE)

	def get_absolute_url(self):
		return "/question/"+str(self.id)

class Answer(models.Model): 
	answer = models.TextField()
	question = models.ForeignKey(Question,on_delete=models.CASCADE)
	answered_by = models.ForeignKey(User,on_delete=models.CASCADE)
	upvotes = models.PositiveIntegerField(default=0)
	downvotes = models.PositiveIntegerField(default=0)

	class Meta:
		constraints = [
			models.UniqueConstraint(fields=['question', 'answered_by'], name='one person one answer')
		]




class Tag(models.Model) : 
	tag_name = models.CharField(max_length=40)


class QuestionTagMap(models.Model):
	 question = models.ForeignKey(Question, on_delete=models.CASCADE)  
	 tag = models.ForeignKey(Tag,on_delete=models.CASCADE)

class AnswerUpvoteDownvoteTable(models.Model):
	reaction_choices = (
		("UPVOTE", "upvote"),
		("DOWNVOTE", "downvote"),
	)
	answer = models.ForeignKey(Answer,on_delete=models.CASCADE)
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	reaction = models.CharField(max_length=9,choices=reaction_choices)


	 		
    
