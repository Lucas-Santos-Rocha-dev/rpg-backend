from django.db import models
from setup.models_abstract import ModeloBase


class Raca(ModeloBase):

    def __str__(self):
        return f"{self.nome}"