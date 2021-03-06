import connexion
import psycopg2
from swagger_server.models.asignatura import Asignatura
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime

# Metodo para conectarnos a la base de datos alumno
def conectar():

    conexion = psycopg2.connect(
        dbname = 'Universidad',
        user = 'postgres',
        password = 'madrid9',
        host='localhost',
        port = '5433'
    )

    return conexion

# Metodo para lanzar los errores
def lanzarError(msg, status, title, typee):
    d = {}
    d["detail"] = msg
    d["error"] = status
    d["title"] = title
    d["type"] = typee
    return d

def get_datos_asignatura(nombre):
    """
    Devuelve una asignatura.
    Devuelve una asignatura por su nombre.
    :param nombre: El nombre de la asignatura
    :type nombre: str

    :rtype: Asignatura
    """
    try:
        conex = conectar()
        cursor = conex.cursor()

        cursor.execute(
            'SELECT * \
             FROM "Asignatura" \
             WHERE nombre =  \''+ nombre + '\';'
        )

        rows = cursor.fetchall()
        conex.close()

        if len(rows) == 0:
                return lanzarError("Asignatura no encontrada",404,"Error","about:blank")
        else:
            return rows

    except Exception as e:
        conex.close()
        print(e)
        return lanzarError(str(e), 404, "Error", "about:blank")


def obtener_asignaturas():
    """
    Obtiene las asignaturas
    Obtiene un listado de las asignaturas de la universidad.
    :param tamanoPagina: Número de asignaturas devueltas
    :type tamanoPagina: int
    :param numeroPaginas: Número de páginas devueltas
    :type numeroPaginas: int

    :rtype: List[Asignatura]
    """
    try:
        conex = conectar()
        cursor = conex.cursor()

        cursor.execute(
            'SELECT * \
             FROM "Asignatura" ;'
        )

        rows = cursor.fetchall()
        conex.close()

        if len(rows) == 0:
            return lanzarError("No hay asignaturas", 404, "Error", "about:blank")
        else:
            return rows

    except Exception as e:
        conex.close()
        print(e)
        return lanzarError(str(e), 404, "Error", "about:blank")
