from rest_framework import serializers
from mightyblade.models import TipoHabilidade


class TipoHabilidadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoHabilidade
        fields = '__all__'
