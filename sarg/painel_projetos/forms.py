from django import forms
from painel_projetos import PROJETOS

class PROJETOSForm(forms.ModelForm):
    class Meta:
        model = PROJETOS
