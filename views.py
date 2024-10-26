from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import Main_contact

# Create your views here.

def home(request):
    return HttpResponse("<h1>Welcome to Home.....</h1>")

def index(request):
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")

#def contact(request):
    #return render(request,"contact.html")
#from .models import contact_master

# Create your views here.
def contact(request):
    if request.method=="POST":
        name=request.POST["name"]
        email=request.POST['email']
        subject=request.POST["subject"]
        website=request.POST["website"]
        message=request.POST["message"]
        
        
        ob=Main_contact.objects.create(name=name,email=email,subject=subject,website=website,message=message)
        ob.save()
        return render(request,"contact.html",{'output':"Register Successful"})
    return render(request,"contact.html")


def gallery(request):
    return render(request,"gallery.html")
def faq(request):
    return render(request,"faq.html")

#def login(request):
    #return render(request,"login.html")
    
#def register(request):
    #return render(request,"register.html")