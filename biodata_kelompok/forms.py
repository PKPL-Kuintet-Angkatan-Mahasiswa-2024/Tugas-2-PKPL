from django import forms

from .models import Biodata, BiodataTheme


class BiodataThemeForm(forms.ModelForm):
    class Meta:
        model = BiodataTheme
        fields = ["primary_color", "font_family"]


class BiodataForm(forms.ModelForm):
    class Meta:
        model = Biodata
        fields = ["nama", "npm"]
