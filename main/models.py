from django.db import models

# Create your models here.

class Arvore(models.Model):
    
    no = models.IntegerField()
    noPai = models.IntegerField()

class Pessoa(models.Model):

    nome = models.CharField(max_length=50)
    sobrenome = models.CharField(max_length=50)
    dataNasc = models.DateTimeField()
    falecido = models.BooleanField()
    dataFalecimento = models.DateTimeField()
    pai = models.CharField(max_length=50)
    mae = models.CharField(max_length=50)
