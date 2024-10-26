from django.shortcuts import render
from .models import contact_master

# Create your views here.
def c_contact(request):
    if request.method=="POST":
        name=request.POST["name"]
        email=request.POST['email']
        mobile=request.POST["mobile"]
        address=request.POST["address"]
        
        
        ob=contact_master.objects.create(name=name,email=email,mobile=mobile,address=address)
        ob.save()
        return render(request,"c_contact.html",{'output':"Register Successful"})
    return render(request,"c_contact.html")