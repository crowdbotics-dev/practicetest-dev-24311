from rest_framework import serializers
from model.models import Newmod

class NewmodSerializer(serializers.ModelSerializer):

    class Meta:
        model = Newmod
        fields = "__all__"