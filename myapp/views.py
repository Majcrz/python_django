from django.shortcuts import render, redirect
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


def login2(request):
    if request.method == "POST":  
        username1=request.POST['username2']
        password1=request.POST['password2']  
        try:
            userdetails= user.objects.get(username=username1,password=password1)
            request.session['userid']=data.id
            return redirect('/home')
        except user.DoesNotExist:
                return render(request, "login2.html",{'status':'Login failed'})
    else:
        return render(request, "login2.html")   

def viewUsers(request):
    userdata2= user.objects.all()
    return render(request,'viewUsers.html',{"userdata2": userdata2})
    



        
