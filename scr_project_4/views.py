from django.shortcuts import get_object_or_404, render, HttpResponseRedirect
from django.http import HttpResponse
from django.template import loader
from scr_app_4.models import *

def assignments(request):
    train_assignments = TrainAssignment.objects.all()
    template = loader.get_template('assignments.html')
    context = {'train_assignments': train_assignments}
    return HttpResponse(template.render(context, request))

def delete_assignment(request, id):
    assignment = get_object_or_404(TrainAssignment, id=id)

    if request.method == "POST":
        assignment.delete()
        return HttpResponseRedirect("/assignments/")

    return render(request, "assignments.html")