from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Pessoa(models.Model):

    usuario_django = models.ForeignKey(User, on_delete=models.CASCADE)
    is_usuario = models.BooleanField()
    pai = models.CharField(max_length=50)
    mae = models.CharField(max_length=50)
    nome = models.CharField(max_length=50)
    sobrenome = models.CharField(max_length=50)
    imagem_url = models.CharField(max_length=50)
    
    def filhos(self):
        pass

    def conjuge(self):
        pass
