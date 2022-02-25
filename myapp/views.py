from django.shortcuts import render
from django.http import HttpResponse

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
        
