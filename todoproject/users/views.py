from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import action
from rest_framework.generics import UpdateAPIView
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework.viewsets import ModelViewSet
from .models import User
from .serializers import UserModelSerializer


class UserModelViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer


class UserAPIView(APIView):
    renderer_classes = [JSONRenderer]

    @action(detail=True, methods=['get'])
    def list(self, request):
        queryset = User.objects.all()
        serializer = UserModelSerializer
        return Response(serializer.data)


class UserUpdateAPIView(UpdateAPIView):
    renderer_classes = [JSONRenderer]
    queryset = User.objects.all()
    serializer_class = UserModelSerializer


