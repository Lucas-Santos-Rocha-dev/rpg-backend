from django.contrib import admin
from .models import (
    CategoriaHabilidade
)


@admin.register(CategoriaHabilidade)
class CategoriaHabilidadeAdmin(admin.ModelAdmin):

    list_display = (
        'nome',
    )
