from django import forms
from .models import Entrepreneur

class EntrepreneurForm(forms.ModelForm):
    class Meta:
        model = Entrepreneur
        fields = [
            'business_name', 'location', 'description', 'lunes_inicio', 'lunes_fin',
            'martes_inicio', 'martes_fin', 'miercoles_inicio', 'miercoles_fin',
            'jueves_inicio', 'jueves_fin', 'viernes_inicio', 'viernes_fin',
            'contact_info', 'logo'
        ]
        widgets = {
            'business_name': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
            'location': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
            'description': forms.Textarea(attrs={'class': 'form-control form-control-sm', 'rows': 3}),
            'lunes_inicio': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control form-control-sm'}),
            'lunes_fin': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control form-control-sm'}),
            'martes_inicio': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control form-control-sm'}),
            'martes_fin': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control form-control-sm'}),
            'miercoles_inicio': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control form-control-sm'}),
            'miercoles_fin': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control form-control-sm'}),
            'jueves_inicio': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control form-control-sm'}),
            'jueves_fin': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control form-control-sm'}),
            'viernes_inicio': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control form-control-sm'}),
            'viernes_fin': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control form-control-sm'}),
            'contact_info': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
            'logo': forms.ClearableFileInput(attrs={'class': 'form-control form-control-sm'}),
        }