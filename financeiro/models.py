from django.db import models

# Create your models here.

class Usuario(models.Model):

    nome = models.CharField(max_length=50)
    cpf = models.CharField(max_length=11)
    data_nasc = models.DateField()
    tel = models.CharField(max_length=11)

class Despesas(models.Model):

    nome_prod = models.CharField(max_length=50)
    quant_prod = models.IntegerField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data_compra = models.DateField()