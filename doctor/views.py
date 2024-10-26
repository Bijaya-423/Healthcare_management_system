from django.shortcuts import render
from signup.models import signup_master

# Create your views here.
def dhome(request):
    name=request.session.get('name')
    #return render(request,"index.html",{'name':name})
    return render(request,"dhome.html",{'name':name})

# def index(request):
#     return render(request,"dhome.html")

# def about(request):
#     return render(request,"about.html")

# def contact(request):
#     return render(request,"contact.html")
# def gallery(request):
#     return render(request,"gallery.html")
# def faq(request):
#     return render(request,"faq.html")

def dviews(request):
    name=request.session.get('name')
    ob=signup_master.objects.get(name=name)
    obj=signup_master.objects.filter(role_name='patient')
    return render(request,"dviews.html",{'user':ob,'data1':obj})