from django import forms
from core.models import Rating, Restaurant

class RestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = ['name', 'restaurant_type']
    
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args,**kwargs)
    #     self.fields['user'].widget.attrs.update({'class':'form-select'})
    #     self.fields['restaurant'].widget.attrs.update({'class':'form-select'})
    #     self.fields['rating'].widget.attrs.update({'class':'form-control'})
        
