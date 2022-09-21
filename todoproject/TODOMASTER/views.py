from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.generics import ListAPIView
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.viewsets import ModelViewSet

from TODOMASTER.models import Project, ToDo
from TODOMASTER.serializers import ProjectHyperlinkedModelSerializer, ToDoModelSerializer


class ProjectLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 10


class ProjectLimitOffsetPaginatonViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectHyperlinkedModelSerializer
    pagination_class = ProjectLimitOffsetPagination


class ProjectKwargsFilterView(ListAPIView):
    serializer_class = ProjectHyperlinkedModelSerializer

    def get_queryset(self):
        name = self.kwargs['name']
        return Project.objects.filter(name__contains=name)


class ProjectModelViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectHyperlinkedModelSerializer


class ToDoLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 20


class ToDoLimitOffsetPaginatonViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ToDoModelSerializer
    pagination_class = ToDoLimitOffsetPagination

    def get_queryset(self):
        name = self.kwargs['name']
        return Project.objects.filter(name__contains=Project)


class ToDoModelViewSet(ModelViewSet):
    queryset = ToDo.objects.all()
    serializer_class = ToDoModelSerializer
