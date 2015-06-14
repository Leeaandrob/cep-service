# coding: utf-8

from .models import Cep
from rest_framework import serializers


class CepSerializer(serializers.HyperlinkedModelSerializer):
    cep = serializers.CharField(source='get_cep', read_only=True)
    zip_code = serializers.CharField()

    class Meta:
        model = Cep
        fields = ('logradouro', 'bairro', 'cidade', 'estado', 'cep', 'zip_code')
        read_only_fields = ('logradouro', 'bairro', 'cidade', 'estado', 'cep')
