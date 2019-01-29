from django.db import models

# Create your models here.

class Usuario(models.Model):
    nome = models.CharField(max_length=50)
    cpf = models.CharField(max_length=11)
    data_nasc = models.DateField()
    tel = models.CharField(max_length=11)