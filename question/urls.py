from django.urls import path 
from . import views 


urlpatterns = [
	path('ask_question/',views.new_question,name='new_question'),
	path('question/<int:question_id>/',views.question,name='question'),
	path('question/<int:question_id>/add_new_answer',views.add_answer,name='add_answer'),
    path('answer/<int:answer_id>/upvote',views.upvote_answer,name='upvote_answer'),
	path('answer/<int:answer_id>/downvote',views.downvote_answer,name='downvote_answer'),
]