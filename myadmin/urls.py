from django.contrib import admin
from django.urls import path 

from myadmin import views as aviews

urlpatterns = [
    #myadmin
    path('aviewdata',aviews.aviewdata,name="aviewdata"),
    path('ahome',aviews.ahome,name="ahome"),
    path('update',aviews.update,name="update"),
    # path('edit',aviews.edit,name="edit"),
    
    
]