from django.db import models
from setup.models_abstract import ModeloBase


class Aventura(ModeloBase):
    mestre = models.CharField('Nome da aventura', max_length=160)
    tipo_aventura = models.ForeignKey('TipoAventura', related_name='aventuras_do_tipo', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Aventura'
        verbose_name_plural = 'Aventuras'
