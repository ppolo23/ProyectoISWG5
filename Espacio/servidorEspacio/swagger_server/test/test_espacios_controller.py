# coding: utf-8

from __future__ import absolute_import

from swagger_server.models.alquilado import Alquilado
from swagger_server.models.espacio import Espacio
from swagger_server.models.reservado import Reservado
from . import BaseTestCase
from six import BytesIO
from flask import json


class TestEspaciosController(BaseTestCase):
    """ EspaciosController integration test stubs """

    def test_alquilar_espacio_put(self):
        """
        Test case for alquilar_espacio_put

        Alquilar un espacio
        """
        alquilado = Alquilado()
        response = self.client.open('/APIespacios/alquilarEspacio',
                                    method='PUT',
                                    data=json.dumps(alquilado),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_espacio_cod_id_get(self):
        """
        Test case for espacio_cod_id_get

        Devuelve un espacio
        """
        response = self.client.open('/APIespacios/espaciosPorId/{codId}'.format(codId='codId_example'),
                                    method='GET')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_espacio_facultad_get(self):
        """
        Test case for espacio_facultad_get

        Devuelve un espacio
        """
        response = self.client.open('/APIespacios/espaciosPorFacultad/{facultad}'.format(facultad='facultad_example'),
                                    method='GET')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_get_espacios_libres(self):
        """
        Test case for get_espacios_libres

        Espacios de una facultad libres
        """
        response = self.client.open('/APIespacios/espacios/libres',
                                    method='GET',
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_get_espacios_ocupados(self):
        """
        Test case for get_espacios_ocupados

        Espacios de una facultad ocupados.
        """
        response = self.client.open('/APIespacios/espacios/ocupados',
                                    method='GET',
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_obtener_espacio(self):
        """
        Test case for obtener_espacio

        Obtiene espacios
        """
        response = self.client.open('/APIespacios/espacios',
                                    method='GET')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_reserva_espacio_put(self):
        """
        Test case for reserva_espacio_put

        Reservar un espacio
        """
        reservado = Reservado()
        response = self.client.open('/APIespacios/reservaEspacio',
                                    method='PUT',
                                    data=json.dumps(reservado),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
