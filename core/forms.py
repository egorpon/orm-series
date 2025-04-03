from django import forms
from core.models import Rating
from crispy_forms.helper import FormHelper

class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['restaurant','user','rating']
    