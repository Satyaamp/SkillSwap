from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import UserRegisterForm, UserProfileForm
from django.contrib.auth.decorators import login_required
from .models import UserProfile

def register_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.set_password(user.password)
            user.save()
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user:
            login(request, user)
            return redirect('home')
    return render(request, 'users/login.html')

@login_required
def profile_view(request):
    profile, created = UserProfile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
    else:
        form = UserProfileForm(instance=profile)
    return render(request, 'users/profile.html', {'form': form, 'profile': profile})

from django.shortcuts import get_object_or_404
from .models import UserProfile
from skills.models import Skill

@login_required
def view_profile(request, user_id):
    profile = get_object_or_404(UserProfile, user__id=user_id, is_public=True, is_banned=False)
    offered_skills = Skill.objects.filter(user=profile.user, is_offered=True)
    wanted_skills = Skill.objects.filter(user=profile.user, is_offered=False)
    return render(request, 'users/view_profile.html', {
        'profile': profile,
        'offered_skills': offered_skills,
        'wanted_skills': wanted_skills,
    })


def logout_view(request):
    logout(request)
    return redirect('login')
