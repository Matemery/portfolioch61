from django.shortcuts import render
from . import models

# Create your views here.
def projects_view(request):
    project_list = models.Project.objects.all()
    context = {'projects': project_list}
    return render(request, 'projects/projects.html', context)


