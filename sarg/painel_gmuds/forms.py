from django import forms
from painel_gmuds import gmuds

class GMUDSForm(forms.ModelForm):
    class Meta:
        model = GMUDS
