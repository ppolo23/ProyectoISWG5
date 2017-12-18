# coding: utf-8

from __future__ import absolute_import

from swagger_server.models.asignatura import Asignatura
from . import BaseTestCase
from six import BytesIO
from flask import json


class TestAsignaturasController(BaseTestCase):
    """ AsignaturasController integration test stubs """

    def test_get_asignatura(self):
        """
        Test case for get_asignatura

        Devuelve una asignatura.
        """
        response = self.client.open('/apiAlumno/asignaturas/{nombre}'.format(nombre='nombre_example'),
                                    method='GET',
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_obtener_asignaturas(self):
        """
        Test case for obtener_asignaturas

        Obtiene las asignaturas
        """
        query_string = [('tamanoPagina', 56),
                        ('numeroPaginas', 56)]
        response = self.client.open('/apiAlumno/asignaturas',
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
