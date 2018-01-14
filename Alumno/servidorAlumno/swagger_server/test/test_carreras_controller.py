# coding: utf-8

from __future__ import absolute_import

from swagger_server.models.carrera import Carrera
from . import BaseTestCase
from six import BytesIO
from flask import json


class TestCarrerasController(BaseTestCase):
    """ CarrerasController integration test stubs """

    def test_get_asignaturas_carrera(self):
        """
        Test case for get_asignaturas_carrera

        Devuelve las asignaturas de la carrera.
        """
        response = self.client.open('/apiAlumno/carreras/{nombre}'.format(nombre='nombre_example'),
                                    method='GET',
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_obtener_carreras(self):
        """
        Test case for obtener_carreras

        Devuelve todas las carreras
        """
        response = self.client.open('/apiAlumno/carreras',
                                    method='GET')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
