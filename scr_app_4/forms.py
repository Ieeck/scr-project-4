from django import forms
from .models import *
import ast

class PlayerForm(forms.ModelForm):

    class Meta:
        model = Player
        fields = '__all__'

class AssignmentForm(forms.ModelForm):
    player = forms.ModelChoiceField(queryset=Player.objects.all())
    unit = forms.ModelChoiceField(queryset=Unit.objects.all())
    route = forms.ModelChoiceField(queryset=Route.objects.all())
    assign_time = forms.DateTimeField(initial=timezone.now())

    class Meta:
        model = TrainAssignment
        fields = ('player', 'unit', 'route', 'assign_time')

class UnitForm(forms.ModelForm):

    class Meta:
        model = Unit
        fields = '__all__'