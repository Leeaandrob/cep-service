# coding: utf-8

from .models import Cep
from rest_framework import serializers


class CepSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cep
        fields = ('pk', 'logradouro', 'bairro', 'cidade', 'estado', 'cep')
