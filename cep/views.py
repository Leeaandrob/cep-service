# coding: utf-8

from rest_framework import viewsets, mixins
from rest_framework import status
from rest_framework.response import Response

from .models import Cep
from .serializers import CepSerializer
from .consulta_ws import consultar_zipcode

import logging

logger = logging.getLogger('console.logger')


class CepViewSet(mixins.RetrieveModelMixin,
                 mixins.ListModelMixin,
                 mixins.CreateModelMixin,
                 mixins.DestroyModelMixin,
                 viewsets.GenericViewSet):
    queryset = Cep.objects.all()
    serializer_class = CepSerializer

    def list(self, request, *args, **kwargs):
        logger.info('Listagem de Ceps')
        response = super(CepViewSet, self).list(request, *args, **kwargs)
        for result in response.data['results']:
            result.pop('zip_code')
        return response

    def retrieve(self, request, *args, **kwargs):
        obj = self.get_object()
        logger.info('Recuperando CEP de: %s' % (obj.pk))
        response = super(CepViewSet, self).retrieve(request, *args, **kwargs)
        response.data.pop('zip_code')
        return response

    def create(self, request, *args, **kwargs):
        logger.info('Criando CEP: %s' % request.data)
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            try:
                resp_json = consultar_zipcode(serializer.data['zip_code'])
                cep = Cep()
                cep.logradouro = resp_json.get('logradouro', u'')
                cep.bairro = resp_json.get('bairro', '')
                cep.cidade = resp_json.get('cidade', u'')
                cep.estado = resp_json.get('estado', u'')
                cep.zip_code = resp_json.get('cep', u'')
                cep.save()

                headers = self.get_success_headers(serializer.data)
                return Response(serializer.data,
                                status=status.HTTP_201_CREATED,
                                headers=headers)
            except Exception:
                return Response({'error': u'CEP Inválido ou não existe'},
                                status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        obj = self.get_object()
        logger.info('Deletando CEP: %s' % obj.pk)
        return super(CepViewSet, self).destroy(request, *args, **kwargs)
