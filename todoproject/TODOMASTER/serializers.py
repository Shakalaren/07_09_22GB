from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer

from TODOMASTER.models import Project, ToDo


class ProjectHyperlinkedModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


class ToDoModelSerializer(ModelSerializer):
    class Meta:
        model = ToDo
        fields = '__all__'
