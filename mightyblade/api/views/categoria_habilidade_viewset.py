from rest_framework import viewsets
from mightyblade.models import CategoriaHabilidade
from ..serializers import CategoriaHabilidadeSerializer
from setup.utils import CustomPagination


class CategoriaHabilidadeViewSet(
    viewsets.ModelViewSet
):

    lookup_field = 'id'
    queryset = CategoriaHabilidade.objects.all().order_by('id')
    serializer_class = CategoriaHabilidadeSerializer
    pagination_class = CustomPagination

    def get_queryset(self):
        qs = CategoriaHabilidade.objects.all().order_by('id')

        aventura_id = self.request.query_params.get('idAventura')

        if aventura_id:
            qs = qs.filter(aventura__id=aventura_id)

        return qs
