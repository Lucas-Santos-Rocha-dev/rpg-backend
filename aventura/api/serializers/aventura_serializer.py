from rest_framework import serializers
from aventura.models import Aventura


class AventuraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aventura
        fields = '__all__'
