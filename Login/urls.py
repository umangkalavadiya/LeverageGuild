from Login import views
from os import name
from django.urls import path
from Login.views import *



urlpatterns = [
    path('', views.home, name='home'),
    path('scholarship', views.scholarship, name='scholarship'),
    path('university', views.university, name='university'),
    path('about', views.about, name='about'),
    path('index', views.index, name='Index'),
    path('signup', views.signUp, name='SignUp'),
    path('login', views.login, name='Login'),
    path('token', views.send_token, name='Token'),
    path('error', views.error, name='Error'),
    path('logout', views.logoutUser, name='Logout'),
    path('verify/<slug>', views.verify, name='Token'),
    path('forgetpass', views.forgetPassword, name='ForgetPassword'),
    path('reset/<token>', views.reset, name='ResetPass'),
    path('parul', views.parul, name='parul'),
     path("generate_essay", views.generate_essay, name="generate_essay"),
     path("iis", views.iis, name="iis"),
     path('bits', views.bits, name='bits'),
     path('amity', views.amity, name='amity'),
     path('Ottawauni', views.Ottawauni, name='Ottawauni'),
     path('UofAuckland', views.UofAuckland, name='UofAuckland'),
     path('UIUCuni', views.UIUCuni, name='UIUCuni'),
     path('Queenmary', views.Queenmary, name='Queenmary'),
     path('Griffithuni', views.Griffithuni, name='Griffithuni'),
  
     
]
