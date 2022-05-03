from rest_framework import authentication
from practicetest.models import Userdetails
from .serializers import UserdetailsSerializer
from rest_framework import viewsets

class UserdetailsViewSet(viewsets.ModelViewSet):
    serializer_class = UserdetailsSerializer
    authentication_classes = (authentication.SessionAuthentication, authentication.TokenAuthentication)
    queryset = Userdetails.objects.all()