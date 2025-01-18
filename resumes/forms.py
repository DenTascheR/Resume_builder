from django import forms
from .models import Resume

class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = ['title', 'summary', 'experience', 'education', 'skills']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'summary': forms.Textarea(attrs={'class': 'form-control'}),
            'experience': forms.Textarea(attrs={'class': 'form-control'}),
            'education': forms.Textarea(attrs={'class': 'form-control'}),
            'skills': forms.Textarea(attrs={'class': 'form-control'}),
        }
