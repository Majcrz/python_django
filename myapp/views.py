from django.shortcuts import render
from django.http import HttpResponse
from .models import user

# Create your views here.
def index(request):
    return HttpResponse('''Congratulations,You have created a web application using django''')


def login(request):

    return render(request,'login.html')


def home(request):

    return render(request,'home.html')    

def login1(request):

    return render(request,'login1.html')    

def sign(request):

    return render(request,'sign_up.html')    

def hello(request):
    if request.method == "POST":
        username=request.POST['username']
        password=request.POST['password']
        fulname=request.POST['full_name']
        age=request.POST['number']
        address=request.POST['address']
        userdata= user(username=username,password=password,full_name=fulname, age=age,address=address)
        userdata.save()
        return render(request,'helo.html')  
    else:
        return render(request,'helo.html')   

def signup(request):
    if request.method == "POST":
        username=request.POST['username']
        password=request.POST['password']
        fulname=request.POST['full_name']
        age=request.POST['number']
        address=request.POST['address']
        datamain= user(username=username,password=password,full_name=fulname, age=age,address=address)
        datamain.save()
        return render(request,'signup.html')  
    else:
        return render(request,'signup.html')         
        
