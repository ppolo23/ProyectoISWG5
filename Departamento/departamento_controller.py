import connexion
from swagger_server.models.alumno import Alumno
from swagger_server.models.departamento import Departamento
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime


def borrar_departamento(codID):
    """
    elimina un departamento
    elimina un departamento de la lista
    :param codID: Código de identificación del departamento a eliminar
    :type codID: str

    :rtype: None
    """
    return 'do some magic!'


def crear_departamento(departamento):
    """
    Crea un departamento
    Añade un departamento a la lista de departamentos
    :param departamento: El departamento que se va a añadir.
    :type departamento: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        departamento = Departamento.from_dict(connexion.request.get_json())

        conex = conectar()
        cursor = conex.cursor()

        cursor.execute("INSERT INTO \"Departamento\" VALUES ("
                    + "'" + str(departamento.id_departamento)+ "',"
                    + "'" + str(departamento.nombre) + "',"
                    + "'" + str(departamento.horasImpartidas)"');")
        
        
        asignaturasUni=["Software","Programacion","Algoritmia"]
        for i in range(0,len(asignaturasUni)):
        	consulta = ' INSERT INTO "Asignatura" VALUES (\'' + str(asignaturasUni[i]) + '\' ;'
            cursor.execute(consulta)

         conex.commit()

    return 'Departamento creado.'


def departamento_cod_id_get(codID):
    """
    Devuelve un departamento
    Devuelve un único departamento identificado por su código de identificación
    :param codID: Número de identificación del departamento
    :type codID: str

    :rtype: Departamento
    """
    return 'do some magic!'


def get_asignaturas_departamento(codID):
    """
    Asignaturas de un departamento
    Devuelve lista con las asignaturas impartidas por el departamento
    :param codID: Código de identificación del departamento que imparte dichas asignaturas
    :type codID: str

    :rtype: List[Departamento]
    """
    return 'do some magic!'


def obtener_departamento(tamagnoPagina=None, numeroPagina=None):
    """
    Obtiene los departamentos
    Obtiene un listado de los departamentos existentes en el sistema
    :param tamagnoPagina: número de departamentos devueltos
    :type tamagnoPagina: int
    :param numeroPagina: número de páginas devueltas
    :type numeroPagina: int

    :rtype: List[Departamento]
    """
    return 'do some magic!'


def recibir_alumno(alumno):
    """
    Asigna grupo al alumno
    Recibe datos alumno y le asigna un grupo de una asignatura determinada
    :param alumno: Datos del alumno y asignatura a matricular
    :type alumno: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        alumno = Alumno.from_dict(connexion.request.get_json())
    return 'do some magic!'
