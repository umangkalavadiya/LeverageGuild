from django import forms
from django.contrib.auth.models import User

from sprofile.models import Sprofile


# class ActivityForm(forms.ModelForm):
#     class Meta:
#         model = Activity
#         fields = ['name']
#         widgets = {
#             'name': forms.CheckboxSelectMultiple
#         }

class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = []

class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Sprofile
       
        fields = ['first_name','last_name', 'email','date_of_birth','gender','address','phone','current_degree','current_gpa','gre_score','ilets_score','research_experience','lor','family_income','sports','speak_french','work_experience','internships']
  

def form_validation_error(form):
    msg = ""
    for field in form:
        for error in field.errors:
            msg += "%s: %s \\n" % (field.label if hasattr(field, 'label') else 'Error', error)
    return msg
