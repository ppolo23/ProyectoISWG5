# coding: utf-8

from __future__ import absolute_import

from swagger_server.models.alumno import Alumno
from swagger_server.models.matricula import Matricula
from . import BaseTestCase
from six import BytesIO
from flask import json


class TestAlumnosController(BaseTestCase):
    """ AlumnosController integration test stubs """

    def test_borrar_alumno(self):
        """
        Test case for borrar_alumno

        elimina un alumno
        """
        response = self.client.open('/apiAlumno/alumno/{dni}'.format(dni='dni_example'),
                                    method='DELETE',
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_get_alumno(self):
        """
        Test case for get_alumno

        Devuelve un alumno.
        """
        response = self.client.open('/apiAlumno/alumno/{dni}'.format(dni='dni_example'),
                                    method='GET',
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_get_alumnos_por_asignatura(self):
        """
        Test case for get_alumnos_por_asignatura

        Alumnos de una asignatura.
        """
        query_string = [('asignatura', 'asignatura_example')]
        response = self.client.open('/apiAlumno/alumno/asignatura',
                                    method='GET',
                                    content_type='application/json',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_get_alumnos_por_carrera(self):
        """
        Test case for get_alumnos_por_carrera

        Alumnos de una carrera.
        """
        query_string = [('carrera', 'carrera_example')]
        response = self.client.open('/apiAlumno/alumno/carrera',
                                    method='GET',
                                    content_type='application/json',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_matricula(self):
        """
        Test case for matricula

        Matriculacion del alumno
        """
        matricula = Matricula()
        response = self.client.open('/apiAlumno/matricula',
                                    method='POST',
                                    data=json.dumps(matricula),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_obtener_alumnos(self):
        """
        Test case for obtener_alumnos

        Obtiene los alumnos
        """
        response = self.client.open('/apiAlumno/alumnos',
                                    method='GET')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_reserva(self):
        """
        Test case for reserva

        Reserva la matricula de un alumno
        """
        alumno = Alumno()
        response = self.client.open('/apiAlumno/reserva',
                                    method='POST',
                                    data=json.dumps(alumno),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
