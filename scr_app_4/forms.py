from django import forms
from .models import Player, TrainAssignment

class PlayerForm(forms.ModelForm):

    class Meta:
        model = Player
        fields = '__all__'