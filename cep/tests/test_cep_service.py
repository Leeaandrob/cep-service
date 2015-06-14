# coding: utf-8

import json

from django.test import TestCase

from rest_framework.test import APIClient

from cep.models import Cep


class TestCreateCep(TestCase):
    def setUp(self):
        self.api_client = APIClient()

    def test_post_zipcode_valido(self):
        resp = self.api_client.post('/api/cep/', {'zip_code': '37550000'},
                                    format='json')
        json_resp = json.loads(resp.content)

        self.assertEqual(resp.status_code, 201)
        self.assertEqual(json_resp['zip_code'], '37550000')
        self.assertEqual(Cep.objects.count(), 1)

    def test_post_zipcode_invalido(self):
        resp = self.api_client.post('/api/cep/', {'zip_code': '1402-260'},
                                    format='json')
        json_resp = json.loads(resp.content)

        self.assertEqual(json_resp['error'], u'CEP Inválido ou não existe')
        self.assertEqual(resp.status_code, 400)

    def test_post_zipcode_vazio(self):
        resp = self.api_client.post('/api/cep/', {'zip_code': ''},
                                    format='json')
        json_resp = json.loads(resp.content)

        self.assertEqual(json_resp['error'], u'CEP Inválido ou não existe')
        self.assertEqual(resp.status_code, 400)


class TestListagemCep(TestCase):
    def setUp(self):
        ceps = ['12345', '09876', '37550000']
        for cep in ceps:
            cep = Cep(logradouro=cep, bairro=cep, cidade=cep, estado=cep,
                      zip_code=cep)
            cep.save()

        self.api_client = APIClient()

    def test_listagem(self):
        resp = self.api_client.get('/api/cep/', format='json')
        print resp.content
        resp_json = json.loads(resp.content)
        self.assertEqual(len(resp_json['results']), 3)

    def test_listagem_paginada(self):
        resp = self.api_client.get('/api/cep/?limit=1', {'limit': '2'},
                                   format='json')
        json_resp = json.loads(resp.content)
        self.assertTrue(json_resp['next'])


class TestGetCep(TestCase):
    def setUp(self):
        zipcodes = ['12345', '09876', '37550000']
        for zipcode in zipcodes:
            cep = Cep(logradouro=zipcode, bairro=zipcode, cidade=zipcode,
                      estado=zipcode, zip_code=zipcode)
            cep.save()

        self.api_client = APIClient()

    def test_get_cep_cadastrado(self):
        resp = self.api_client.get('/api/cep/37550000/', format='json')
        json_resp = json.loads(resp.content)

        self.assertEqual(resp.status_code, 200)
        self.assertEqual(json_resp['logradouro'], '37550000')

    def test_get_cep_nao_cadastrado(self):
        resp = self.api_client.get('/api/cep/37550001/', format='json')
        json_resp = json.loads(resp.content)

        self.assertEqual(resp.status_code, 404)
        self.assertEqual(json_resp['detail'], u'Não encontrado.')


class TestDeleteCep(TestCase):
    def setUp(self):
        zipcode = '37550000'
        cep = Cep(logradouro=zipcode, bairro=zipcode, cidade=zipcode,
                  estado=zipcode, zip_code=zipcode)
        cep.save()

        self.api_client = APIClient()

    def test_delete_cep(self):
        resp = self.api_client.delete('/api/cep/37550000/', format='json')

        self.assertEqual(resp.status_code, 204)
        self.assertEqual(Cep.objects.count(), 0)

    def test_delete_cep_inexistente(self):
        resp = self.api_client.delete('/api/cep/37550001/', format='json')

        self.assertEqual(resp.status_code, 404)
        self.assertEqual(Cep.objects.count(), 1)
