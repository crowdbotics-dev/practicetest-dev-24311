from rest_framework import authentication
from model.models import Newmod
from .serializers import NewmodSerializer
from rest_framework import viewsets

class NewmodViewSet(viewsets.ModelViewSet):
    serializer_class = NewmodSerializer
    authentication_classes = (authentication.SessionAuthentication, authentication.TokenAuthentication)
    queryset = Newmod.objects.all()