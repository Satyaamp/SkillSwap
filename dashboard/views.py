from django.shortcuts import render

# Create your views here.
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, redirect
from django.contrib.admin.views.decorators import staff_member_required
from users.models import UserProfile
from skills.models import Skill
from swaps.models import SwapRequest
from .forms import BroadcastMessageForm
from django.http import HttpResponse
import csv

@staff_member_required
def admin_dashboard(request):
    users = UserProfile.objects.all()
    skills = Skill.objects.all()
    swaps = SwapRequest.objects.all()
    return render(request, 'dashboard/dashboard.html', {
        'users': users,
        'skills': skills,
        'swaps': swaps
    })

@staff_member_required
def toggle_skill_approval(request, skill_id):
    skill = Skill.objects.get(id=skill_id)
    skill.approved = not skill.approved
    skill.save()
    return redirect('admin_dashboard')

@staff_member_required
def toggle_user_ban(request, user_id):
    profile = UserProfile.objects.get(user__id=user_id)
    profile.is_banned = not profile.is_banned
    profile.save()
    return redirect('admin_dashboard')

@staff_member_required
def broadcast_message(request):
    if request.method == 'POST':
        form = BroadcastMessageForm(request.POST)
        if form.is_valid():
            # Optionally: save in a model, send email, or display
            return render(request, 'dashboard/broadcast_success.html', {'form': form})
    else:
        form = BroadcastMessageForm()
    return render(request, 'dashboard/broadcast.html', {'form': form})

@staff_member_required
def export_data_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="platform_data.csv"'

    writer = csv.writer(response)
    writer.writerow(['User', 'Location', 'Public', 'Skills Offered', 'Skills Wanted'])

    for profile in UserProfile.objects.all():
        offered = Skill.objects.filter(user=profile.user, is_offered=True)
        wanted = Skill.objects.filter(user=profile.user, is_offered=False)
        writer.writerow([
            profile.user.username,
            profile.location,
            profile.is_public,
            ", ".join([s.name for s in offered]),
            ", ".join([s.name for s in wanted])
        ])

    return response
