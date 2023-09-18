from rest_framework import viewsets
from mightyblade.models import TipoHabilidade
from ..serializers import TipoHabilidadeSerializer
from setup.utils import CustomPagination


class TipoHabilidadeViewSet(
    viewsets.ModelViewSet
):

    lookup_field = 'id'
    queryset = TipoHabilidade.objects.all().order_by('id')
    serializer_class = TipoHabilidadeSerializer
    pagination_class = CustomPagination

    def get_queryset(self):
        qs = TipoHabilidade.objects.all().order_by('id')

        aventura_id = self.request.query_params.get('idAventura')

        if aventura_id:
            qs = qs.filter(aventura__id=aventura_id)

        return qs
