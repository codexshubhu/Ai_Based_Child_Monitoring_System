# core/forms.py
from django import forms
from .models import ActivityReport, Child, ChildMilestone

class ActivityReportForm(forms.ModelForm):
    class Meta:
        model = ActivityReport
        fields = ['child', 'activities_done', 'notes', 'image']
        widgets = {
            'activities_done': forms.Textarea(attrs={'rows': 4, 'class': 'form-control'}),
            'notes': forms.Textarea(attrs={'rows': 2, 'class': 'form-control'}),
            'child': forms.Select(attrs={'class': 'form-select'}),
        }

class ChildMilestoneForm(forms.ModelForm):
    class Meta:
        model = ChildMilestone
        fields = ['milestone', 'status']
        widgets = {
            'milestone': forms.Select(attrs={'class': 'form-select'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
        }