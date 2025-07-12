from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from .models import SwapRequest
from skills.models import Skill
from users.models import UserProfile

@login_required
def create_swap(request, receiver_id):
    if request.method == 'POST':
        offered_skill_id = request.POST.get('offered_skill')
        requested_skill_id = request.POST.get('requested_skill')
        message = request.POST.get('message', '')
        
        try:
            offered_skill = Skill.objects.get(id=offered_skill_id)
            requested_skill = Skill.objects.get(id=requested_skill_id)
            receiver = UserProfile.objects.get(id=receiver_id).user
            
            swap = SwapRequest.objects.create(
                sender=request.user,
                receiver=receiver,
                offered_skill=offered_skill,
                requested_skill=requested_skill,
                message=message
            )
            messages.success(request, 'Swap request sent successfully!')
            return redirect('swap_dashboard')
        except (Skill.DoesNotExist, UserProfile.DoesNotExist):
            messages.error(request, 'Invalid skill or user selected.')
    
    return render(request, 'swaps/create_swap.html')

@login_required
def swap_dashboard(request):
    sent_swaps = SwapRequest.objects.filter(sender=request.user)
    received_swaps = SwapRequest.objects.filter(receiver=request.user)
    
    context = {
        'sent_swaps': sent_swaps,
        'received_swaps': received_swaps,
    }
    return render(request, 'swaps/dashboard.html', context)

@login_required
def update_swap_status(request, swap_id, status):
    swap = get_object_or_404(SwapRequest, id=swap_id)
    
    # Only the receiver can update the status
    if swap.receiver != request.user:
        messages.error(request, 'You are not authorized to update this swap.')
        return redirect('swap_dashboard')
    
    if status in ['accepted', 'rejected']:
        swap.status = status
        swap.save()
        messages.success(request, f'Swap {status} successfully!')
    else:
        messages.error(request, 'Invalid status.')
    
    return redirect('swap_dashboard')

@login_required
def cancel_swap(request, swap_id):
    swap = get_object_or_404(SwapRequest, id=swap_id)
    
    # Only the sender can cancel the swap
    if swap.sender != request.user:
        messages.error(request, 'You are not authorized to cancel this swap.')
        return redirect('swap_dashboard')
    
    if swap.status == 'pending':
        swap.status = 'cancelled'
        swap.save()
        messages.success(request, 'Swap cancelled successfully!')
    else:
        messages.error(request, 'Cannot cancel a swap that is not pending.')
    
    return redirect('swap_dashboard')

