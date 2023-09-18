from rest_framework import viewsets
from aventura.models import TipoAventura
from ..serializers import TipoAventuraSerializer
from setup.utils import CustomPagination, info_to_json
from rest_framework.decorators import action
from rest_framework.response import Response


class TipoAventuraViewSet(
    viewsets.ModelViewSet
):

    lookup_field = 'id'
    queryset = TipoAventura.objects.all().order_by('id')
    serializer_class = TipoAventuraSerializer
    pagination_class = CustomPagination

    @action(detail=False, url_path='tabelas',)
    def tabelas(self, request):
        from ...models import TipoAventura

        result = {
            'tipos_aventura': info_to_json(TipoAventura.SISTEMA_CHOICES)
        }

        return Response(result)
