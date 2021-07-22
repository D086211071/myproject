from django import forms
from .models import registerforms
class employeeform(forms.ModelForm):
    class Meta:
        model=registerforms
        fields="__all__"