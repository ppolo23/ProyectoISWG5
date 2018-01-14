# coding: utf-8

from __future__ import absolute_import

from swagger_server.models.alumno import Alumno
from swagger_server.models.departamento import Departamento
from . import BaseTestCase
from six import BytesIO
from flask import json


class TestDepartamentoController(BaseTestCase):
    """ DepartamentoController integration test stubs """

    def test_asignar_grupo(self):
        """
        Test case for asignar_grupo

        Asigna grupo al alumno
        """
        alumno = Alumno()
        response = self.client.open('/dep/Alumno/asignarGrupo',
                                    method='POST',
                                    data=json.dumps(alumno),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_borrar_departamento(self):
        """
        Test case for borrar_departamento

        elimina un departamento
        """
        response = self.client.open('/dep/departamento/{codID}'.format(codID='codID_example'),
                                    method='DELETE',
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_crear_departamento(self):
        """
        Test case for crear_departamento

        Crea un departamento
        """
        departamento = Departamento()
        response = self.client.open('/dep/departamento',
                                    method='POST',
                                    data=json.dumps(departamento),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_departamento_cod_id_get(self):
        """
        Test case for departamento_cod_id_get

        Devuelve un departamento
        """
        response = self.client.open('/dep/departamento/{codID}'.format(codID='codID_example'),
                                    method='GET')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_get_asignaturas_departamento(self):
        """
        Test case for get_asignaturas_departamento

        Asignaturas de un departamento
        """
        query_string = [('codID', 'codID_example')]
        response = self.client.open('/dep/departamento/asignaturas',
                                    method='GET',
                                    content_type='application/json',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_obtener_departamento(self):
        """
        Test case for obtener_departamento

        Obtiene los departamentos
        """
        query_string = [('tamagnoPagina', 56),
                        ('numeroPagina', 56)]
        response = self.client.open('/dep/departamentos',
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
