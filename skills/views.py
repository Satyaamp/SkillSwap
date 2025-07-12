from django.shortcuts import render, redirect
from .forms import SkillForm
from .models import Skill
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from users.models import UserProfile

@login_required
def add_skill(request):
    if request.method == 'POST':
        form = SkillForm(request.POST)
        if form.is_valid():
            skill = form.save(commit=False)
            skill.user = request.user
            skill.save()
            return redirect('browse_skills')
    else:
        form = SkillForm()
    return render(request, 'skills/add_skill.html', {'form': form})

def browse_skills(request):
    query = request.GET.get('q')
    availability = request.GET.get('availability')

    profiles = UserProfile.objects.filter(is_public=True, is_banned=False)
    if availability:
        profiles = profiles.filter(availability=availability)

    if query:
        users_with_skills = Skill.objects.filter(name__icontains=query).values_list('user', flat=True)
        profiles = profiles.filter(user__in=users_with_skills)

    skills = Skill.objects.filter(user__in=[p.user for p in profiles], is_offered=True)
    return render(request, 'skills/browse.html', {
        'skills': skills,
        'query': query,
        'availability': availability,
    })
