from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from scr_app_4.models import *

def home(request):
    temp = "TemporaryVariable"
    train_assignments = TrainAssignment.objects.all()
    template = loader.get_template('temp.html')
    context = {'temp': temp, 'train_assignments': train_assignments}
    return HttpResponse(template.render(context, request))