from django.urls import path 
from . import views 


urlpatterns = [
	path('bio/',views.view_bio,name='view_bio'),
	path('',views.login,name='login'),
	path('signup',views.signup,name='signup'),
]