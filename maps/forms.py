from django import forms
from .models import AptMap

class MapForm(forms.ModelForm):
    class Meta:
        model = AptMap
        fields = ('complex_name', 'complex_address', 'complex_map')