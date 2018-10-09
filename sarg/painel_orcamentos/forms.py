from django import forms
from painel_oracamentos import ORCAMENTOS

class ORCAMENTOSForm(forms.ModelForm):
    class Meta:
        model = ORCAMENTOS
#class ORCAMENTOSForm(forms.ModelForm)
#    valor = forms.DecimalField(max_digits=10, decimal_places=2, localize=True)
#    class Meta:
#        model = ORCAMENTOS
