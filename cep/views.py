# coding: utf-8

from rest_framework import viewsets

from .models import Cep
from .serializers import CepSerializer

import logging

logger = logging.getLogger('console.logger')


class CepViewSet(viewsets.ModelViewSet):
    queryset = Cep.objects.all()
    serializer_class = CepSerializer

    def list(self, request, *args, **kwargs):
        logger.info('Listagem de Ceps')
        return super(CepViewSet, self).list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        obj = self.get_object()
        logger.info('Recuperando CEP de: %d' % (obj.pk))
        return super(CepViewSet, self).retrieve(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        logger.info('Criando CEP: %s' % request.data)

        return super(CepViewSet, self).create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        obj = self.get_object()
        logger.info('Atualizando CEP: %d com os dados: %s'
                    % (obj.pk, request.data))
        return super(CepViewSet, self).update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        obj = self.get_object()
        logger.info('Deletando CEP: %d' % obj.pk)
        return super(CepViewSet, self).destroy(request, *args, **kwargs)
