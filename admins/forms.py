from django import forms

from City.models import City
from .models import Admin

class City(forms.ModelForm):
  prefix = 'city'
  class Meta:
    model = City
    fields = ['name']
  def __init__(self, *args, **kwargs):
    super(City, self).__init__(*args, **kwargs)
    self.fields['name'].widget.attrs.update({'class': 'form-control', 'id': 'city_name'})
    #self.fields['name'].required = False

class AddAdmin(forms.ModelForm):

  class Meta:
    model = Admin
    fields = ['name','email','is_main','password','image']
  def __init__(self, *args, **kwargs):
    super(AddAdmin, self).__init__(*args, **kwargs)
    self.fields['name'].widget.attrs.update({'class': 'form-control'})
    self.fields['email'].widget.attrs.update({'class': 'form-control'})
    self.fields['password'].widget.attrs.update({'class': 'form-control'})
    self.fields['image'].widget.attrs.update({'class': 'form-control'})
    self.fields['is_main'].widget.attrs.update({'class': 'form-check-input'})
