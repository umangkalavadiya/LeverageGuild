from django.urls import path
from sprofile import views

appname = 'sprofile'
urlpatterns = [
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    
]
