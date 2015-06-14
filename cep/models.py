# coding: utf-8
from django.db import models

# Create your models here.


class Cep(models.Model):
    logradouro = models.CharField(max_length=150)
    bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)
    cep = models.CharField(max_length=10)
