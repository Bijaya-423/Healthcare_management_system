"""
URL configuration for healthcare_management_system project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path ,include

from home import views as hviews
from add.views import add
#or
#from add import views as aviews
from add.views import sub,animated,buttonripple
from add.views import calculator,animation,autotexteffect



from contact import views as cviews




#from doctor import views as dviews
from patient import views as pviews




urlpatterns = [
    
    path('myadmin/', include('myadmin.urls')),
    path('appointment/', include('appointment.urls')),
    path('doctor/', include('doctor.urls')),
    path('patient/', include('patient.urls')),
    path('login/', include('login.urls')),
    path('signup/', include('signup.urls')),
    
    path('admin/', admin.site.urls),
    #Home app
    path('home',hviews.home),
    path('',hviews.index),
    path('about',hviews.about),
    path('contact',hviews.contact),
    path('gallery',hviews.gallery),
    path('faq',hviews.faq),
    #path('register',hviews.register),
    
    #add app
    path('add',add),
    path('sub',sub),
    path('calculator',calculator),
    path('animation',animation),
    path('animated',animated),
    path('buttonripple',buttonripple),
    path('autotexteffect',autotexteffect),
    
    
   
    
    #contact
    path('ccontact',cviews.c_contact),
    
    
    
    
    
    
    
    
    
    
    
    
]
