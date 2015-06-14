# coding: utf-8
import requests

CEP_SERVICE_URL = 'http://api.postmon.com.br/v1/cep/%s'


def consultar_zipcode(zipcode):
    resp = requests.get(CEP_SERVICE_URL % zipcode)
    if resp.status_code == 200:
        dados = resp.json()
        if 'statusText' in dados and dados['statusText'] == 'error':
            raise Exception(u'CEP não existe')
        return dados
    raise Exception(u'Não foi possível consultar o serviço')
