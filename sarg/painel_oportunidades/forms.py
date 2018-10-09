from django import forms
from painel_oportunidades import OPORTUNIDADES

class OPORTUNIDADESForm(forms.ModelForm):
    class Meta:
        model = OPORTUNIDADES
