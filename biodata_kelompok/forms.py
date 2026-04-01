from django import forms
from .models import BiodataTheme, Biodata 

class BiodataForm(forms.ModelForm): 
    class Meta:
        model = BiodataTheme
        fields = ['primary_color', 'font_family']