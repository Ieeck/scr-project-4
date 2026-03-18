from django import forms
from .models import *
import ast

class PlayerForm(forms.ModelForm):

    class Meta:
        model = Player
        fields = '__all__'

class DestringModelChoiceField(forms.ModelChoiceField):
    def to_python(self, unit):
        unit = ast.literal_eval(unit) # some strange form of magic...
        return super().to_python(unit) # that will remove the tuple from the string

class AssignmentForm(forms.ModelForm):
    player = forms.ModelChoiceField(queryset=Player.objects.all())
    unit = DestringModelChoiceField(queryset=Unit.objects.all())
    route = forms.ModelChoiceField(queryset=Route.objects.all())
    assign_time = forms.DateTimeField(initial=timezone.now())

    class Meta:
        model = TrainAssignment
        fields = ('player', 'unit', 'route', 'assign_time')