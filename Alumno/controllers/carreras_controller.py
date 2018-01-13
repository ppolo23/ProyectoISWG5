import connexion
import psycopg2
from swagger_server.models.asignatura import Asignatura
from swagger_server.models.carrera import Carrera
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
        host ='localhost',
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

def get_asignaturas_carrera(nombre):
    """
    Devuelve las asignaturas de la carrera.
    Devuelve las asignaturas de la carrera pasada por parametro.
    :param nombre: El nombre de la carrera
    :type nombre: str

    :rtype: List[str]
    """
    try:
        conex = conectar()
        cursor = conex.cursor()

        carrera = ["informatica","telecomunicaciones", "industrial"]
        codigo = 0

        for i in range(0,3):
            if (carrera[i] in nombre):
                codigo = i+1

        if (codigo == 0):
            return lanzarError("Carrera no encontrada", 404, "Error", "about:blank")

        cursor.execute(
            'SELECT "Asignatura".nombre \
             FROM "Asignatura" INNER JOIN "Pertenece_" ON "Asignatura"."CodAsignatura" = "Pertenece_"."CodAsignatura" \
             WHERE "Pertenece_"."CodCarrera" =  '+ str(codigo) + ';'
        )

        rows = cursor.fetchall()
        conex.close()

        if len(rows) == 0:
            return lanzarError("Carrera no encontrada", 404, "Error", "about:blank")
        else:
            return rows

    except Exception as e:
        conex.close()
        print(e)
        return lanzarError(str(e), 404, "Error", "about:blank")


def obtener_carreras():
    """
    Devuelve todas las carreras
    Devuelve todas las carreras de la Universidad
    :param tamanoPagina: Número de carreras devueltas
    :type tamanoPagina: int
    :param numeroPaginas: Número de páginas devueltas
    :type numeroPaginas: int

    :rtype: List[Carrera]
    """
    try:
        conex = conectar()
        cursor = conex.cursor()

        cursor.execute(
            'SELECT * \
             FROM "Carrera";'
        )

        rows = cursor.fetchall()
        conex.close()

        if len(rows) == 0:
            return lanzarError("No hay carreras", 404, "Error", "about:blank")
        else:
            return rows

    except Exception as e:
        conex.close()
        print(e)
        return lanzarError(str(e), 404, "Error", "about:blank")