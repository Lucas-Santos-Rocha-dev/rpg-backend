from django.db import models
from setup.models_abstract import ModeloBase


class CategoriaHabilidade(ModeloBase):
    aventura = models.ForeignKey(
        'aventura.Aventura', related_name='categorias_de_habilidade_da_aventura', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nome}"
