import connexion
import psycopg2
from swagger_server.models.asignatura import Asignatura
from swagger_server.models.carrera import Carrera
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime

#Metodo para conectarnos a la base de datos alumno
def conectar():

    conexion = psycopg2.connect(dbname = 'Universidad',user = 'postgres', password = 'madrid9',host='localhost',port = '5433')

    return conexion


#Metodo para lanzar los errores
def lanzarError(msg, status, title, typee):
    d = {}
    d["detail"] = msg
    d["error"] = status
    d["title"] = title
    d["type"] = typee
    return d



def get_asignaturas_carrera(nombre):
    """
    Devuelve asignaturas pertenecientes a la carrera
    Devuelve asignaturas de la carrera pasada por parametro
    :param nombre: El nombre de la carrera
    :type nombre: str

    :rtype: List[Asignatura]
    """
    conex=conectar()
    cursor=conex.cursor()

    consulta='SELECT * FROM "Carrera" WHERE nombre =  \''+ nombre + '\';'

    cursor.execute(
        consulta
        )

    rows = cursor.fetchall()

    conex.close()

    if len(rows)==0:
            return lanzarError("Carrera no encontrada",404,"Error","about:blank")

    else:
        return row_to_json(rows)
    


def get_carreras(tamanoPagina=None, numeroPaginas=None):
    """
    Devuelve todas las carreras
    Devuelve todas las carreras de la Universidad
    :param tamanoPagina: Número de carreras devueltas
    :type tamanoPagina: int
    :param numeroPaginas: Número de páginas devueltas
    :type numeroPaginas: int

    :rtype: List[Carrera]
    """

    conex = conectar()
    cursor = conex.cursor()

    consulta1= 'SELECT * FROM "Carrera" ;'
    cursor.execute(
        consulta1
       )

    rows = cursor.fetchall()

    conex.close()

    if len(rows) == 0:
        return lanzarError("No hay carreras", 404, "Error", "about:blank")

    else:
        return row_to_json(rows)