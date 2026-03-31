from django import forms
from biodata_kelompok.models import Biodata


class BiodataForm(forms.ModelForm):
    class Meta:
        model = Biodata
        fields = ['bio']
