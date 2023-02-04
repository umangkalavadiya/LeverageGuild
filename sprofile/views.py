from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import View
from django.urls import reverse
from .forms import *
from .models import Sprofile

@method_decorator(login_required(login_url='login'), name='dispatch')
class EditProfile(View):
    profile = None

    def dispatch(self, request, *args, **kwargs):
        self.profile, __ = Sprofile.objects.get_or_create(user=request.user)
        return super(EditProfile, self).dispatch(request, *args, **kwargs)



def edit_profile(request):
    profile, created = Sprofile.objects.get_or_create(user=request.user)
    user_form = ProfileForm(instance=request.user)
    sprofile_form = EditProfileForm(instance=profile)

    if request.method == 'POST':
        user_form = ProfileForm(request.POST, instance=request.user)
        sprofile_form = EditProfileForm(request.POST, instance=profile)

        if user_form.is_valid() and sprofile_form.is_valid():
            
            user_form.save()
            sprofile_form.save()
            return redirect('/edit_profile/')

    context = {'user_form': user_form, 'sprofile_form': sprofile_form}
    return render(request, 'edit_profile.html', context)

