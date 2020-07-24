from django.conf import settings
from django.db import models
from django.utils import timezone 
from user.models import User
from question.model import Question 
import os

class Comment(models.Model): 
	comment = models.TextField()  
	commented_by = models.ForeignKey(User)
	upvotes = models.PositiveIntegerField(default=0)
    downvotes = models.PositiveIntegerField(default=0) 