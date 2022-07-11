from django.db import models
from uuid import uuid4

class Herois(models.Model):
    idHeroi = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    nomeHeroi = models.CharField(max_length=255)
    poder = models.CharField(max_length=255)
    descricao = models.CharField(max_length=255)
    idade = models.IntegerField()
    urlImagem = models.CharField(max_length=255)
