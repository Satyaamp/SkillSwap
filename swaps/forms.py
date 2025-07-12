from django import forms
from .models import SwapRequest, Feedback
from skills.models import Skill

class SwapRequestForm(forms.ModelForm):
    class Meta:
        model = SwapRequest
        fields = ['offered_skill', 'requested_skill', 'message']

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['rating', 'comment']
