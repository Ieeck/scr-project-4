from django.shortcuts import get_object_or_404, render, HttpResponseRedirect
from django.http import HttpResponse
from django.template import loader
from scr_app_4.forms import *

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

def create_assignment(request):
    if request.method == "GET":
        template = loader.get_template('create_assignment.html')
        context = {'form': AssignmentForm()}
        return HttpResponse(template.render(context, request))

    elif request.method == "POST":
        form = AssignmentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/assignments/")
        else:
            template = loader.get_template('create_assignment.html')
            context = {'form': form}
            return HttpResponse(template.render(context, request))


def players(request):
    players_get = Player.objects.all()
    template = loader.get_template('players.html')
    context = {'players': players_get}
    return HttpResponse(template.render(context, request))

def delete_player(request, username):
    player = get_object_or_404(Player, username=username)

    if request.method == "POST":
        player.delete()
        return HttpResponseRedirect("/players/")

    return render(request, "players.html")

def create_player(request):
    if request.method == "GET":
        template = loader.get_template('create_player.html')
        context = {'form': PlayerForm()}
        return HttpResponse(template.render(context, request))

    elif request.method == "POST":
        form = PlayerForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/players/")
        else:
            template = loader.get_template('create_player.html')
            context = {'form': form}
            return HttpResponse(template.render(context, request))

def units(request):
    units_get = Unit.objects.all()
    template = loader.get_template('units.html')
    context = {'units': units_get}
    return HttpResponse(template.render(context, request))

def delete_unit(request, id):
    unit = get_object_or_404(Unit, id=id)

    if request.method == "POST":
        unit.delete()
        return HttpResponseRedirect("/units/")

    return render(request, "units.html")

def create_unit(request):
    if request.method == "GET":
        template = loader.get_template('create_unit.html')
        context = {'form': UnitForm()}
        return HttpResponse(template.render(context, request))

    elif request.method == "POST":
        form = UnitForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/units/")
        else:
            template = loader.get_template('create_unit.html')
            context = {'form': form}
            return HttpResponse(template.render(context, request))