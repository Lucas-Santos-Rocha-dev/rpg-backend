from django.db import models
from setup.models_abstract import ModeloBase


class TipoHabilidade(ModeloBase):
    aventura = models.ForeignKey(
        'aventura.Aventura', related_name='tipos_habilidade_da_aventura', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nome}"
