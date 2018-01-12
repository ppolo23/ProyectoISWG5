# coding: utf-8

from __future__ import absolute_import

from swagger_server.models.espacio import Espacio
from . import BaseTestCase
from six import BytesIO
from flask import json


class TestEspacioController(BaseTestCase):
    """ EspacioController integration test stubs """

    def test_insertar_cobro_espacio(self):
        """
        Test case for insertar_cobro_espacio

        Insertar registro de cobro de espacio
        """
        reservado = Espacio()
        response = self.client.open('/apiPagos/insertarCobroEspacio',
                                    method='PUT',
                                    data=json.dumps(reservado),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_pago_espacio(self):
        """
        Test case for pago_espacio

        Consulta pago/alquiler espacio.
        """
        response = self.client.open('/apiPagos/espacio/{id_espacio}'.format(id_espacio=56),
                                    method='GET',
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
