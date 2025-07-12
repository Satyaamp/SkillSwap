from django import forms
from .models import Skill

class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ['name', 'is_offered']
        labels = {
            'name': 'Skill Name',
            'is_offered': 'Type of Skill',
        }
        widgets = {
            'is_offered': forms.Select(choices=[(True, "Offered"), (False, "Wanted")])
        }
