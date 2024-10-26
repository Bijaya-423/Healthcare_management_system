from django.shortcuts import render,redirect
from signup.models import signup_master
# Create your views here.

def ahome(request):
    name=request.session.get('name')
    return render(request,"ahome.html",{'name':name})

def aviewdata(request):
    ob=signup_master.objects.all()
    if request.method=="POST":
        btn=request.POST['btn']
        if btn=='edit':
            email=request.POST['email']
            ob=signup_master.objects.get(email=email)
            return render(request,'edit.html',{'data1':ob})
        if btn=='delete':
            email=request.POST['email']
            ob=signup_master.objects.get(email=email).delete()
            return redirect('aviewdata')
    return render(request,"aviewdata.html",{'data':ob})

def update(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        mobile=request.POST['mobile']
        role_name=request.POST['role_name']
        ob=signup_master.objects.filter(email=email).update(name=name,mobile=mobile,role_name=role_name)
        return redirect(aviewdata)
        
    return render(request,"aviewdata.html")
