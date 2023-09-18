from rest_framework import serializers
from mightyblade.models import CategoriaHabilidade


class CategoriaHabilidadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriaHabilidade
        fields = '__all__'
