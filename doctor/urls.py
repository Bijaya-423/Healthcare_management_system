from django.contrib import admin
from django.urls import path 

from doctor import views as ddviews

urlpatterns = [
    #doctor
    path('doctorindex',ddviews.dhome,name="dhome"),
    #path('index',dviews.index,name="index"),
    path('dviews',ddviews.dviews,name="dviews")
    
    
    
    
]