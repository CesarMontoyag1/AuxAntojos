from django import forms
from .models import Entrepreneur

class EntrepreneurForm(forms.ModelForm):
    class Meta:
        model = Entrepreneur
        fields = ['business_name', 'location', 'lunes', 'martes', 'miercoles', 'jueves', 'viernes', 'contact_info']
        widgets = {
            'business_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: Galletas Mora'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: Salida bloque 33'}),
            'lunes': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: 10:00 am - 4:00 pm'}),
            'martes': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: 10:00 am - 4:00 pm'}),
            'miercoles': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: 10:00 am - 4:00 pm'}),
            'jueves': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: 10:00 am - 4:00 pm'}),
            'viernes': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: 10:00 am - 4:00 pm'}),
            'contact_info': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: numero celular'}),
        } 
        
        