from django import forms
from .models import *

class ClientForm(forms.ModelForm):
    class Meta:
        model = client
        exclude = [""]