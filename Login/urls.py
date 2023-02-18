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
     path('griffin_s', views.griffin_s,name='griffin_s'),
     path('amity_s', views.amity_s, name='amity_s'),
     path('auckland_s', views.auckland_s, name='auckland_s'),
     path('iis_s', views.iis_s, name='iis_s'),
     path('parul_s',views.parul_s,name='parul_s'),
     path('queen_s', views.queen_s, name='queen_s'),
    path('uuic_s',views.uuic_s,name='uuic_s'),
    path('bits_s',views.bits_s,name='bits_s'),
    path('ottawa_s',views.ottawa_s,name='ottawa_s'),
    path('interview',views.interview,name='interview'),
  
     
]
