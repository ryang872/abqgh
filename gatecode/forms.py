from django import forms
from .models import addGate

class gateForm(forms.ModelForm):
    class Meta:
        model = addGate
        fields = ('complex', 'code', 'address')