from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def home(request):
    temp = "TemporaryVariable"
    template = loader.get_template('temp.html')
    context = {'temp': temp}
    return HttpResponse(template.render(context, request))

