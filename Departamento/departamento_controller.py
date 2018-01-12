import connexion
import psycopg2
from swagger_server.models.alumno import Alumno
from swagger_server.models.asignatura import Asignatura
from swagger_server.models.departamento import Departamento
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime


def conectar():

    conexion = psycopg2.connect(
        database = "espacios",
        user = "postgres",
        password = "postgres",
        host = "127.0.0.1",
        port = "5432"
    )

    return conexion

def lanzarError(msg, status, title, typee):
    """
    Lanza un mensaje de \"error\" en forma de json
    """
    d = {}
    d["detail"] = msg
    d["error"] = status
    d["title"] = title
    d["type"] = typee
    return d

def borrar_departamento(codID):
    """
    elimina un departamento
    elimina un departamento de la lista
    :param codID: Código de identificación del departamento a eliminar
    :type codID: str

    :rtype: None
    """
    conex = conectar()
    cursor = conex.cursor()

    cursor.execute(
        "DELETE \
         FROM Departamento \
         WHERE id_departamento = " + str(codID) + ";"
    )

    rows = cursor.fetchall()

    conex.commit()
    conex.close()

    return 'Alumno con dni: {}, ha sido borrado del sistema'.format(dni)


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
    conex = conectar()
    cursor = conex.cursor()

    cursor.execute(
        "SELECT row_to_json(Departamento) \
         FROM Departamento \
         WHERE id_departamento = " + str(codID) + ";"
    )

    rows = cursor.fetchall()

    conex.close()

    if len(rows) == 0:
        return lanzarError("Departamento no encontrado", 404, "Error", "about:blank")

    else:
        return rows[0][0]


def get_asignaturas_departamento(codID):
    """
    Asignaturas de un departamento
    Devuelve lista con las asignaturas impartidas por el departamento
    :param codID: Código de identificación del departamento que imparte dichas asignaturas
    :type codID: str

    :rtype: List[Asignatura]
    """
    conex = conectar()
    cursor = conex.cursor()

    cursor.execute(
        "SELECT array_to_json(array_agg(row_to_json(t))) \
         FROM (SELECT row_to_json(Asignatura.nombre) \
         FROM Departamento, Asignatura \
         WHERE Asignatura.id_departamento = " + str(codID) + "AND Asignatura.id_departamento = Departamento.id_departamento) as t;"
    )

    rows = cursor.fetchall()

    conex.close()

    if len(rows) == 0:
        return lanzarError("Departamento no encontrado", 404, "Error", "about:blank")

    else:
        return rows[0][0]


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
    conex = conectar()
    cursor = conex.cursor()

    cursor.execute(
        'SELECT  id_departamento, nombre, "horasImpartidas"\
         FROM "Departamento" ;'
    )

    rows = cursor.fetchall()

    conex.close()

    if len(rows) == 0:
        return lanzarError("No hay departamentos", 404, "Error", "about:blank")

    else:
        return rows



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
