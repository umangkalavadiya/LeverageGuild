from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import View
from .forms import *
from .models import Sprofile
from .forms import ProfileForm
from joblib import load


@method_decorator(login_required(login_url='login'), name='dispatch')
class ProfileView(View):
    edit_profile = None

    def dispatch(self, request, *args, **kwargs):
        self.edit_profile, __ = Sprofile.objects.get_or_create(user=request.user)
        return super(ProfileView, self).dispatch(request, *args, **kwargs)

    def get(self, request):
        context = {'edit_profile': self.edit_profile, 'segment': 'edit_profile'}
        return render(request, 'edit_profile.html', context)

    def post(self, request):
        form = ProfileForm(request.POST, request.FILES, instance=self.edit_profile)

        if form.is_valid():
            edit_profile = form.save()
           

            messages.success(request, 'Profile saved successfully')
            return redirect('/edit_profile')
        else:
            messages.error(request, form_validation_error)
            
            
        context = {'edit_profile': self.edit_profile, 'form': form, 'segment': 'edit_profile'}
        return render(request, 'edit_profile.html', context)



def edit_profile(request):
    if request.user.is_authenticated:
        profile, created = Sprofile.objects.get_or_create(user=request.user)
        if request.method == 'POST':
            form = ProfileForm(request.POST, instance=profile)
            if form.is_valid():
                form.save()
                return redirect('Login:Index')
        else:
            form = ProfileForm(instance=profile)
        return render(request, 'edit_profile.html', {'form': form})
    else:
        return redirect('Login:Login')
    
import pickle

def au(request): 
    if request.user.is_authenticated:
        cgpa = float(Sprofile.objects.get(user=request.user).current_gpa)
        ilets_score = int(Sprofile.objects.get(user=request.user).ilets_score)
        gate_score = int(Sprofile.objects.get(user=request.user).gate_score)
        lor = int(Sprofile.objects.get(user=request.user).lor)
        research_experience = int(Sprofile.objects.get(user=request.user).research_experience)
        work_experience = int(Sprofile.objects.get(user=request.user).work_experience)
        course = 1
        university = 1
        
        # Load the saved model
        loaded_model = load(open("sprofile/AU.pickle", "rb"))
        # loaded_model = load("sprofile/uni_rec_model.joblib")
        
        # Use the model to make a prediction
        result = loaded_model.predict([[cgpa, ilets_score,gate_score,lor, research_experience, work_experience, course, university]])
    
        # Render the result on the HTML template
        return render(request, "predict.html", {"result": result}) 
    else:
        return redirect('Login:Login') 
    
    
def bits(request): 
    if request.user.is_authenticated:
        cgpa = float(Sprofile.objects.get(user=request.user).current_gpa)
        gate_score = int(Sprofile.objects.get(user=request.user).gate_score)
        lor = int(Sprofile.objects.get(user=request.user).lor)
        research_experience = int(Sprofile.objects.get(user=request.user).research_experience)
        work_experience = int(Sprofile.objects.get(user=request.user).work_experience)
        course = 1
        university = 1
        
        # Load the saved model
        loaded_model = load(open("sprofile/BITS.pickle", "rb"))
        # loaded_model = load("sprofile/uni_rec_model.joblib")
        
        # Use the model to make a prediction
        result = loaded_model.predict([[cgpa, gate_score, lor, research_experience, work_experience, course, university]])
    
        # Render the result on the HTML template
        return render(request, "predict.html", {"result": result}) 
    else:
        return redirect('Login:Login')   


def gu(request): 
    if request.user.is_authenticated:
        cgpa = float(Sprofile.objects.get(user=request.user).current_gpa)
        ilets_score = int(Sprofile.objects.get(user=request.user).ilets_score)
        lor = int(Sprofile.objects.get(user=request.user).lor)
        research_experience = int(Sprofile.objects.get(user=request.user).research_experience)
        work_experience = int(Sprofile.objects.get(user=request.user).work_experience)
        course = 1
        university = 1
        
        # Load the saved model
        loaded_model = load(open("sprofile/GU.pickle", "rb"))
        # loaded_model = load("sprofile/uni_rec_model.joblib")
        
        # Use the model to make a prediction
        result = loaded_model.predict([[cgpa, ilets_score,lor, research_experience, work_experience, course, university]])
    
        # Render the result on the HTML template
        return render(request, "predict.html", {"result": result}) 
    else:
        return redirect('Login:Login')  
    
    
def iis(request): 
    if request.user.is_authenticated:
        cgpa = float(Sprofile.objects.get(user=request.user).current_gpa)
        ilets_score = int(Sprofile.objects.get(user=request.user).ilets_score)
        gate_score = int(Sprofile.objects.get(user=request.user).gate_score)
        lor = int(Sprofile.objects.get(user=request.user).lor)
        research_experience = int(Sprofile.objects.get(user=request.user).research_experience)
        work_experience = int(Sprofile.objects.get(user=request.user).work_experience)
        course = 1
        university = 1
        
        # Load the saved model
        loaded_model = load(open("sprofile/IIS.pickle", "rb"))
        # loaded_model = load("sprofile/uni_rec_model.joblib")
        
        # Use the model to make a prediction
        result = loaded_model.predict([[cgpa, ilets_score,gate_score,lor, research_experience, work_experience, course, university]])
    
        # Render the result on the HTML template
        return render(request, "predict.html", {"result": result}) 
    else:
        return redirect('Login:Login')      

def pu(request): 
    if request.user.is_authenticated:
        cgpa = float(Sprofile.objects.get(user=request.user).current_gpa)
        gate_score = int(Sprofile.objects.get(user=request.user).gate_score)
        lor = int(Sprofile.objects.get(user=request.user).lor)
        research_experience = int(Sprofile.objects.get(user=request.user).research_experience)
        work_experience = int(Sprofile.objects.get(user=request.user).work_experience)
        course = 1
        university = 1
        
        # Load the saved model
        loaded_model = load(open("sprofile/PU.pickle", "rb"))
        # loaded_model = load("sprofile/uni_rec_model.joblib")
        
        # Use the model to make a prediction
        result = loaded_model.predict([[cgpa, gate_score,lor, research_experience, work_experience, course, university]])
    
        # Render the result on the HTML template
        return render(request, "predict.html", {"result": result}) 
    else:
        return redirect('Login:Login')  

def qmu(request): 
    if request.user.is_authenticated:
        cgpa = float(Sprofile.objects.get(user=request.user).current_gpa)
        ilets_score = int(Sprofile.objects.get(user=request.user).ilets_score)
        lor = int(Sprofile.objects.get(user=request.user).lor)
        research_experience = int(Sprofile.objects.get(user=request.user).research_experience)
        work_experience = int(Sprofile.objects.get(user=request.user).work_experience)
        course = 1
        university = 1
        
        # Load the saved model
        loaded_model = load(open("sprofile/QMU.pickle", "rb"))
        # loaded_model = load("sprofile/uni_rec_model.joblib")
        
        # Use the model to make a prediction
        result = loaded_model.predict([[cgpa, ilets_score,lor, research_experience, work_experience, course, university]])
    
        # Render the result on the HTML template
        return render(request, "predict.html", {"result": result}) 
    else:
        return redirect('Login:Login')  

def su(request): 
    if request.user.is_authenticated:
        cgpa = float(Sprofile.objects.get(user=request.user).current_gpa)
        ilets_score = int(Sprofile.objects.get(user=request.user).ilets_score)
        gre_score = int(Sprofile.objects.get(user=request.user).gre_score)
        lor = int(Sprofile.objects.get(user=request.user).lor)
        research_experience = int(Sprofile.objects.get(user=request.user).research_experience)
        work_experience = int(Sprofile.objects.get(user=request.user).work_experience)
        course = 1
        university = 1
        
        # Load the saved model
        loaded_model = load(open("sprofile/SU.pickle", "rb"))
        # loaded_model = load("sprofile/uni_rec_model.joblib")
        
        # Use the model to make a prediction
        result = loaded_model.predict([[cgpa, ilets_score,gre_score,lor, research_experience, work_experience, course, university]])
    
        # Render the result on the HTML template
        return render(request, "predict.html", {"result": result}) 
    else:
        return redirect('Login:Login')  

def uoo(request): 
    if request.user.is_authenticated:
        cgpa = float(Sprofile.objects.get(user=request.user).current_gpa)
        ilets_score = int(Sprofile.objects.get(user=request.user).ilets_score)
        gre_score = int(Sprofile.objects.get(user=request.user).gre_score)
        lor = int(Sprofile.objects.get(user=request.user).lor)
        research_experience = int(Sprofile.objects.get(user=request.user).research_experience)
        work_experience = int(Sprofile.objects.get(user=request.user).work_experience)
        course = 1
        university = 1
        
        # Load the saved model
        loaded_model = load(open("sprofile/UOO.pickle", "rb"))
        # loaded_model = load("sprofile/uni_rec_model.joblib")
        
        # Use the model to make a prediction
        result = loaded_model.predict([[cgpa, ilets_score,gre_score,lor, research_experience, work_experience, course, university]])
    
        # Render the result on the HTML template
        return render(request, "predict.html", {"result": result}) 
    else:
        return redirect('Login:Login')  


def uiuc(request): 
    if request.user.is_authenticated:
        cgpa = float(Sprofile.objects.get(user=request.user).current_gpa)
        ilets_score = int(Sprofile.objects.get(user=request.user).ilets_score)
        gre_score = int(Sprofile.objects.get(user=request.user).gre_score)
        lor = int(Sprofile.objects.get(user=request.user).lor)
        research_experience = int(Sprofile.objects.get(user=request.user).research_experience)
        work_experience = int(Sprofile.objects.get(user=request.user).work_experience)
        course = 1
        university = 1
        
        # Load the saved model
        loaded_model = load(open("sprofile/UIUC.pickle", "rb"))
        # loaded_model = load("sprofile/uni_rec_model.joblib")
        
        # Use the model to make a prediction
        result = loaded_model.predict([[cgpa, ilets_score,gre_score,lor, research_experience, work_experience, course, university]])
    
        # Render the result on the HTML template
        return render(request, "predict.html", {"result": result}) 
    else:
        return redirect('Login:Login')  


