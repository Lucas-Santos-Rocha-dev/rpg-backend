from django.contrib import admin
from .models import (
    Aventura,
    TipoAventura
)


@admin.register(Aventura)
class AventuraAdmin(admin.ModelAdmin):

    def get_tipo_aventura_nome(self, obj):
        return obj.tipo_aventura.nome if obj and obj.tipo_aventura.nome else ''

    def get_tipo_aventura_sistema_utilizado(self, obj):
        return obj.tipo_aventura.sistema_utilizado if obj and obj.tipo_aventura.sistema_utilizado else ''

    get_tipo_aventura_nome.short_description = 'Tipo Aventura'
    get_tipo_aventura_sistema_utilizado.short_description = 'Sistema utilizado'

    list_display = (
        'nome',
        'mestre',
        'get_tipo_aventura_nome',
        'get_tipo_aventura_sistema_utilizado'
    )


@admin.register(TipoAventura)
class TipoAventuraAdmin(admin.ModelAdmin):

    list_display = (
        'nome',
        'sistema_utilizado'
    )
