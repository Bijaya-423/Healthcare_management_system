from django.shortcuts import render
from .models import signup_master

# Create your views here.
def signup(request):
    if request.method=="POST":
        name=request.POST["name"]
        email=request.POST["email"]
        mobile=request.POST["mobile"]
        password=request.POST["password"]
        role_name=request.POST["role_name"]
        
        obj=signup_master.objects.create(name=name,email=email,mobile=mobile,password=password,role_name=role_name)
        obj.save()
        return render(request,"login.html",{'output':"Register Successful"})
        
    return render(request,"signup.html")
