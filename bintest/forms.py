from django import forms
  
# import GeeksModel from models.py
from .models import PollingUnit
  
# create a ModelForm
class PollingUnitForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = PollingUnit
        fields = "__all__"