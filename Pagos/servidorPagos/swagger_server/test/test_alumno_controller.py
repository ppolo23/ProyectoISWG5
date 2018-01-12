# coding: utf-8

from __future__ import absolute_import

from swagger_server.models.alumno import Alumno
from . import BaseTestCase
from six import BytesIO
from flask import json


class TestAlumnoController(BaseTestCase):
    """ AlumnoController integration test stubs """

    def test_insertar_cobro_matricula(self):
        """
        Test case for insertar_cobro_matricula

        Insertar registro de cobro de matricula
        """
        reservado = Alumno()
        response = self.client.open('/apiPagos/insertarCobroMatricula',
                                    method='PUT',
                                    data=json.dumps(reservado),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_pago_alumno(self):
        """
        Test case for pago_alumno

        Consulta el pago del alumno
        """
        response = self.client.open('/apiPagos/alumno/{dni}'.format(dni='dni_example'),
                                    method='GET',
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
