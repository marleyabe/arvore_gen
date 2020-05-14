from django.db import models
from django.conf import settings

# Create your models here.
FAMILIARES = [
	('1', 'Pai'),
	('2', 'Mae')
]

class Familia(models.Model):
    generos = models.CharField(choices=FAMILIARES, max_length=10)

class Pessoa(models.Model):
    nome = models.CharField(max_length=200)
    sobrenome = models.CharField(max_length=200)
    parentesco = models.ForeignKey(Familia, on_delete=models.CASCADE)

