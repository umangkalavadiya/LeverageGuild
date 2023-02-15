from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext as _
from decimal import Decimal
 
    
class Sprofile(models.Model):
    
    user = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE,default = None)
    
     # Personal Information
    first_name = models.CharField(max_length=255,default=None,blank=True, null=True)
    last_name = models.CharField(max_length=255,default=None,blank=True, null=True)
    # email = models.EmailField(max_length=255,default=None,blank=True, null=True)
    date_of_birth = models.DateField(default=None,blank=True, null=True)
    gender = models.CharField(max_length=255,default=None,blank=True, null=True)
    address = models.TextField(max_length=255,default=None,blank=True, null=True)
    phone = models.CharField(max_length=20,default=None,blank=True, null=True)
    
    
    # Academic Information
    current_degree = models.TextField(max_length=255,default=None,blank=True, null=True)
    current_gpa = models.DecimalField(max_digits=3, decimal_places=2,default=0.00,blank=True, null=True)
    gre_score = models.IntegerField(default=None,blank=True, null=True)
    gate_score = models.IntegerField(default=None,blank=True, null=True)
    ilets_score = models.IntegerField(default=None,blank=True, null=True)
    research_experience = models.BooleanField(default=0,blank=True, null=True)
    lor = models.IntegerField(default=None,blank=True, null=True)
    
    # Financial Information
    family_income = models.IntegerField(default=None,blank=True, null=True)
   
    
    # Extra Curricular Activities
    sports = models.BooleanField(default=0,blank=True, null=True)
    speak_french = models.BooleanField(default=0,blank=True, null=True)
    
  
    
    # Work Experience and Internship
    work_experience = models.BooleanField(default=0,blank=True, null=True)
    internships = models.BooleanField(default=0,blank=True, null=True)
    
    id = models.AutoField(primary_key=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _('Sprofile')
        verbose_name_plural = _('Sprofiles')


    