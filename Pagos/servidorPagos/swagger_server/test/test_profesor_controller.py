# coding: utf-8

from __future__ import absolute_import

from swagger_server.models.profesor import Profesor
from . import BaseTestCase
from six import BytesIO
from flask import json


class TestProfesorController(BaseTestCase):
    """ ProfesorController integration test stubs """

    def test_cobro_nomina(self):
        """
        Test case for cobro_nomina

        Consulta pago nomina
        """
        response = self.client.open('/apiPagos/profesor/{dni}'.format(dni='dni_example'),
                                    method='GET')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_insertar_nomina_profesor(self):
        """
        Test case for insertar_nomina_profesor

        Insertar registro de nomina profesor
        """
        reservado = Profesor()
        response = self.client.open('/apiPagos/insertarNominaProfesor',
                                    method='PUT',
                                    data=json.dumps(reservado),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
