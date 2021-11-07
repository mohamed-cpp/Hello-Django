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
  password = forms.CharField(widget=forms.PasswordInput())
  class Meta:
    model = Admin
    fields = ['name','email','is_main','password','image']
  def __init__(self, *args, **kwargs):
    self._newly_created = kwargs.get('instance') is None
    super(AddAdmin, self).__init__(*args, **kwargs)
    self.fields['name'].widget.attrs.update({'class': 'form-control'})
    self.fields['email'].widget.attrs.update({'class': 'form-control'})
    self.fields['password'].widget.attrs.update({'class': 'form-control'})
    self.fields['image'].widget.attrs.update({'class': 'form-control'})
    self.fields['is_main'].widget.attrs.update({'class': 'form-check-input'})
    if not self._newly_created:
      self.fields['password'].required = False
      self.fields['image'].widget.initial_text = "currently"
      forms.ImageField(label='Image Admin',required=False, error_messages = {'invalid':"Image files only"}, widget=forms.FileInput)


class UslessForm(forms.Form):
  prefix = 'testform'
  email = forms.EmailField(label="Email")
  password = forms.CharField(widget = forms.PasswordInput())
  file = forms.FileField(label="File")
  data = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
