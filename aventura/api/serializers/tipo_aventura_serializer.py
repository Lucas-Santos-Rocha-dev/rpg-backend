from rest_framework import serializers
from aventura.models import TipoAventura


class TipoAventuraSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoAventura
        fields = '__all__'
