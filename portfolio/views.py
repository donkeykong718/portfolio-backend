from rest_framework import viewsets

from .serializers import TechSerializer, ProjectSerializer
from .models import Tech, Project

# Create your views here.


class TechViewSet(viewsets.ModelViewSet):
    queryset = Tech.objects.all()
    serializer_class = TechSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
