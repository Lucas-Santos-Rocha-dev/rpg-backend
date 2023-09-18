from rest_framework import viewsets
from aventura.models import Aventura
from ..serializers import AventuraSerializer
from setup.utils import CustomPagination


class AventuraViewSet(
    viewsets.ModelViewSet
):

    lookup_field = 'id'
    queryset = Aventura.objects.all().order_by('id')
    serializer_class = AventuraSerializer
    pagination_class = CustomPagination
