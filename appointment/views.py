from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
#from .forms import AppointmentForm
from .models import Appointment



# Create your views here.
def book_appointment(request):
    if request.method=="POST":
        name=request.POST["name"]
        email=request.POST["email"]
        phone=request.POST["phone"]
        date=request.POST["date"]
        time=request.POST["time"]
        department=request.POST["department"]
        obj=Appointment.objects.create(name=name,email=email,phone=phone,date=date,time=time,department=department)
        obj.save()
        return render(request,"book_appointment.html",{'output':"Appointment Register Successful"})
    
    return render(request,"book_appointment.html")