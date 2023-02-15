from django.urls import path
from sprofile import views

appname = 'sprofile'
urlpatterns = [
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    # path('predicted/', views.predicted, name='predicted'),
    path('au/', views.au, name='au'),
    path('bits/', views.bits, name='bits'),
    path('gu/', views.gu, name='gu'),
    path('iis/', views.iis, name='iis'),
    path('qmu/', views.qmu, name='qmu'),
    path('pu/', views.pu, name='pu'),
    path('su/', views.su, name='su'),
    path('uoo/', views.uoo, name='uoo'),
    path('uiuc/', views.uiuc, name='uiuc'),
]
