from django.db import models
from setup.models_abstract import ModeloBase


class TipoAventura(ModeloBase):

    # Sistema utilizado choice
    SISTEMA_MIGHTYBLADE = 'MIGHTYBLADE'
    SISTEMA_NARUTO = 'NARUTO'

    SISTEMA_NOMES = {
        SISTEMA_MIGHTYBLADE: 'Mightyblade',
        SISTEMA_NARUTO: 'Naruto'
    }

    SISTEMA_CHOICES = (
        (SISTEMA_MIGHTYBLADE, SISTEMA_NOMES[SISTEMA_MIGHTYBLADE]),
        (SISTEMA_NARUTO, SISTEMA_NOMES[SISTEMA_NARUTO]),
    )

    sistema_utilizado = models.CharField(
        'Sistema utilizado',
        max_length=50,
        choices=SISTEMA_CHOICES,
        default=SISTEMA_MIGHTYBLADE
    )

    # condicionar qual raça mostrar pelo tipo de sistema

    class Meta:
        verbose_name = 'TipoAventura'
        verbose_name_plural = 'TipoAventuras'
