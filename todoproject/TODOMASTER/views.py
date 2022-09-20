from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet

from TODOMASTER.models import Project, ToDo
from TODOMASTER.serializers import ProjectHyperlinkedModelSerializer, ToDoModelSerializer


class ProjectModelViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectHyperlinkedModelSerializer


class ToDoModelViewSet(ModelViewSet):
    queryset = ToDo.objects.all()
    serializer_class = ToDoModelSerializer
