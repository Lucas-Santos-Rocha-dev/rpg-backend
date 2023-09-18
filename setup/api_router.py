from rest_framework import routers

from mightyblade.api.views import CategoriaHabilidadeViewSet, TipoHabilidadeViewSet
from aventura.api.views import AventuraViewSet, TipoAventuraViewSet


router = routers.DefaultRouter()
router.register('tipo-aventuras', TipoAventuraViewSet, basename='TipoAventuras')
router.register('aventuras', AventuraViewSet, basename='Aventuras')
router.register('categorias-habilidades', CategoriaHabilidadeViewSet, basename='CategoriasHabilidades')
router.register('tipos-habilidades', TipoHabilidadeViewSet, basename='TiposHabilidades')


app_name = "api"
urlpatterns = router.urls
