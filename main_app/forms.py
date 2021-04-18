from django.forms import ModelForm
from .models import Walking


class WalkingForm(ModelForm):
    class Meta:
        model = Walking
        fields = ['date', 'time', 'potty']
