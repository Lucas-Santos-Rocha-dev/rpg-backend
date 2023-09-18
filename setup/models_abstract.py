from django.db import models


class TemCriadoEm(models.Model):
    criado_em = models.DateTimeField("Criado em", editable=False, auto_now_add=True)

    class Meta:
        abstract = True


class TemAtivo(models.Model):
    ativo = models.BooleanField("Está ativo?", default=True)

    class Meta:
        abstract = True


class TemAlteradoEm(models.Model):
    alterado_em = models.DateTimeField("Alterado em", editable=False, auto_now=True)

    class Meta:
        abstract = True


class ModeloBase(TemCriadoEm, TemAlteradoEm):
    nome = models.CharField('Nome', max_length=160)
    descricao = models.TextField(blank=True)

    # Expoe explicitamente o model manager para evitar falsos alertas de Unresolved attribute reference for class Model
    objects = models.Manager()

    @classmethod
    def by_id(cls, id):
        return cls.objects.get(id=id)

    class Meta:
        abstract = True
