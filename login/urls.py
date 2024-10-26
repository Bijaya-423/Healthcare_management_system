from django.contrib import admin
from django.urls import path ,include

from login import views as lviews

urlpatterns = [
    
    #login
    path('login',lviews.login, name="login"),
    path('login1',lviews.login1,name="login1"),
    
]