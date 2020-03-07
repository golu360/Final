from django.contrib.auth.forms import forms
from .models import File




class DiagnosisForm(forms.Form):
    image = forms.ImageField(required=True)

    class Meta:
        model = File
        fields = ['image']