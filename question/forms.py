from django import forms  

class QuestionForm(forms.Form):
	question = forms.CharField(max_length=200)  
	tags = forms.CharField(max_length=20)
