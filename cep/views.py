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
