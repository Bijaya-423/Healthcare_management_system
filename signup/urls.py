from django.contrib import admin
from django.urls import path ,include

from signup import views as sviews


urlpatterns = [
 #signup
    path('signup',sviews.signup,name="signup"),
    
]