from django.forms import ModelForm
from need.models import Need

class NeedForm(ModelForm):
    class Meta:
        model = Need
        fields = ('need',)




    