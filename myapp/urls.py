from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('login',views.login,name='login'),
    path('home',views.home,name='home'),
    path('login1',views.login1,name='login1'),
    path('sign',views.sign,name='sign'),
    path('hello',views.hello,name='hello'),
    path('signup',views.signup,name='signup'),
    path('login2',views.login2,name='login2'),
]

