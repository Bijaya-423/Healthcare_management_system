from django.contrib import admin
from django.urls import path 

from patient import views as ppviews

urlpatterns = [
    #patient
    #patient
    path('patientindex',ppviews.phome,name="phome"),
    path('pviews',ppviews.pviews,name="pviews")
    
    
    
    
]