from django.conf import settings
from django.db import models
from django.utils import timezone 
from user.models import User
from question.model import Question 
import os

class Answer(models.Model):
	answer = models.TextField() 
	answered_by = models.ForeignKey(User)
	question = models.ForeignKey(Question)
	upvotes = models.PositiveIntegerField(default=0)
    downvotes = models.PositiveIntegerField(default=0)

