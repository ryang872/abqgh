from django import forms
from .models import noTip

class tipForm(forms.ModelForm):
    class Meta:
        model = noTip
        fields = ('first', 'last', 'address', 'screenshot')
        # exclude = ['user',]

