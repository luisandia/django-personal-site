from django.shortcuts import render
from .models import Project
import json

from django.core import serializers

def portfolio(request):
    projects = Project.objects.all()
    data = serializers.serialize('json', projects)


    return render(request, "portfolio/portfolio.html", {'projects': projects,'serialized':data})
