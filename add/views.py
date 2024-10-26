from django.shortcuts import render

# Create your views here.

def add(request):
    if request.method == "POST":
        a=int(request.POST['fno'])
        b=int(request.POST['sno'])
        result=a+b
        return render(request,"add.html" ,{"output":result})  
    return render(request,"add.html")

def sub(request):
    if request.method=="POST":
        x=int(request.POST['fno'])
        y=int(request.POST['sno'])
        result=x-y
        return render(request,"add.html" ,{"output":result}) 
    return render(request,"add.html")

def calculator(request):
    if request.method == "POST":   
        a=int(request.POST['fno'])
        b=int(request.POST['sno']) 
    
        if "add" in request.POST:
            result = a+b
        elif "sub" in request.POST:
            result = a-b
        elif "mul" in request.POST:
            result = a*b
        elif "div" in request.POST:
            result = a//b
        #else :
           # result="can not devided by zero"
        return render(request,'calculator.html',{"output":result})
    
    return render(request,"calculator.html")

def animation(request):
    return render(request,"animation.html")

def animated(request):
    return render(request,"animated.html")

def buttonripple(request):
    return render(request,"buttonripple.html")

def autotexteffect(request):
    return render(request,"autotexteffect.html")