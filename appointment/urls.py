from django.contrib import admin
from django.urls import path ,include

from appointment import views as apviews


urlpatterns = [
    
    path('appointment',apviews.book_appointment,name="appointment"),
    
    
]