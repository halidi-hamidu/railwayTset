from django.forms import ModelForm
from .models import *
class RailwayForm(ModelForm):
    class Meta:
        models =RailwayModel
        fields = '__all__'