import connexion
import requests
import json
import psycopg2

from swagger_server.models.alquilado import Alquilado
from swagger_server.models.espacio import Espacio
from swagger_server.models.reservado import Reservado
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime

apiBase = "http://localhost:6000/apiPagos/"
headers = {'Authorization': 'Bearer ', "Content-Type": "application/json", "data":"data"}


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

def alquilar_espacio_put(alquilado):
    """
    Alquilar un espacio
    Alquila un unico espacio mediante un registro json
    :param alquilado: Espacio que se necesita alquilar
    :type alquilado: dict | bytes

    :rtype: None
    """

    if connexion.request.is_json:
        alquilado = Alquilado.from_dict(connexion.request.get_json())

        conex = conectar()
        cursor = conex.cursor()

        try:
            cursor.execute(
                "INSERT INTO alquilados VALUES (" + str(alquilado.cod_id) +
                                        ",\'" + str(alquilado.fecha) + "\'" +
                                        ",\'" + str(alquilado.hora_inicio) + "\'" +
                                        ",\'" + str(alquilado.hora_fin) + "\'" + 
                                        "," + str(alquilado.id_prof) + ");"
            )

            datos = {
                "cod_id": alquilado.cod_id,
                "fecha": alquilado.fecha,
                "hora": alquilado.hora_inicio,
                "id_prof": alquilado.id_prof,
                "cantidad": 10
            }

            r = requests.put(apiBase + "insertarCobroEspacio", data=json.dumps(datos), headers=headers)
            print(r)

        except Exception as e:
             print(e)
             return lanzarError(str(e), 404, "Error", "about:blank")
            
        conex.commit()
        conex.close()

        return {"status":"Alquiler correcto"}


def espacio_cod_id_get(codId):
    """
    Devuelve un espacio
    Devuelve un unico espacio identificado por su codId de espacio
    :param codId: Numero de identificacion del espacio
    :type codId: str
    :rtype: Espacio
    """

    conex = conectar()
    cursor = conex.cursor()

    try:
        cursor.execute(
            "SELECT row_to_json(espacios) \
             FROM espacios \
             WHERE cod_id = " + str(codId) + ";"
        )

        rows = cursor.fetchall()

    except Exception as e:
        print(e)
        return lanzarError(str(e), 404, "Error", "about:blank")

    conex.close()

    if len(rows) == 0:
        return lanzarError("Espacio no encontrado", 404, "Error", "about:blank")

    else:
        return rows[0][0]


def espacio_facultad_get(facultad):
    """
    Devuelve un espacio
    Devuelve un unico espacio identificado por la facultad a la que pertenece
    :param facultad: facultad del espacio
    :type facultad: str

    :rtype: Espacio
    """
    conex = conectar()
    cursor = conex.cursor()

    try:
        cursor.execute(
            "SELECT array_to_json(array_agg(row_to_json(espacios))) \
             FROM \"espacios\" \
            WHERE espacios.facultad = '" + str(facultad) + "';"
        )

        rows = cursor.fetchall()

    except Exception as e:
        print(e)
        return lanzarError(str(e), 404, "Error", "about:blank")

    conex.close()

    if len(rows) == 0:
        return lanzarError("Espacio no encontrado", 404, "Error", "about:blank")

    else:
        return rows[0][0]


def get_espacios_ocupados():
    """
    Espacios de una facultad ocupados.
    Devuelve los espacios ocupados de la facultad.

    :rtype: List[Espacio]
    """
    conex = conectar()
    cursor = conex.cursor()

    try:
        cursor.execute(
            "SELECT array_to_json(array_agg(row_to_json(t)))\
             FROM (SELECT DISTINCT espacios.cod_id, espacios.nombre, espacios.facultad, tipo, capacidad, preciohora\
                  FROM espacios, reservados, alquilados\
                  WHERE espacios.cod_id = reservados.cod_id OR espacios.cod_id = alquilados.cod_id) as t;"
        )

        rows = cursor.fetchall()


    except Exception as e:
        print(e)
        return lanzarError(str(e), 404, "Error", "about:blank")

    conex.close()

    if rows == None:
        return lanzarError("No hay espacios ocupados", 404, "Error", "about:blank")

    else:
        return rows[0][0]

def get_espacios_libres():
    """
    Espacios de una facultad libres
    Devuelve los espacios ocupados de la facultad.

    :rtype: List[Espacio]
    """
    conex = conectar()
    cursor = conex.cursor()

    try:
        cursor.execute(
            "SELECT array_to_json(array_agg(row_to_json(t)))\
             FROM (SELECT espacios.cod_id, espacios.nombre, espacios.facultad, tipo, capacidad, preciohora\
                   FROM espacios\
                   WHERE espacios.cod_id NOT IN (SELECT cod_id FROM alquilados) AND \
                         espacios.cod_id NOT IN (SELECT cod_id FROM reservados) \
                   ) as t;"
        )

        rows = cursor.fetchall()

    except Exception as e:
        print(e)
        return lanzarError(str(e), 404, "Error", "about:blank")

    conex.close()

    if len(rows) == 0:
        return lanzarError('No hay espacios libres', 404, 'Error',
                           'about:blank')
    else:
        return rows[0][0]


def obtener_espacio():
    """
    Obtiene espacios
    Obtiene un listado de espacios del sistema.

    :rtype: List[Espacio]
    """
    conex = conectar()
    cursor = conex.cursor()

    try:
        cursor.execute(
            "SELECT array_to_json(array_agg(row_to_json(espacios))) \
            FROM espacios ;"
        )

        rows = cursor.fetchall()  #lista de elementos que contiene la query
    except Exception as e:
        print(e)
        return lanzarError(str(e), 404, "Error", "about:blank")

    conex.close()

    if len(rows) == 0:
        return lanzarError("No hay espacios", 404, "Error", "about:blank")

    else:
        return rows[0][0]


def reserva_espacio_put(reservado):
    """
    Reservar un espacio
    Reserva un unico espacio mediante un registro json
    :param reservado: Espacio que se necesita reservar
    :type reservado: dict | bytes
    :rtype: None
    """
    if connexion.request.is_json:
        reservado = Reservado.from_dict(connexion.request.get_json())

        conex = conectar()
        cursor = conex.cursor()

        try:
            cursor.execute(
                "INSERT INTO reservados VALUES (" + str(reservado.cod_id) +
                                            ",\'" + str(reservado.fecha_inicio) + "\'" +
                                            ",\'" + str(reservado.dia_semana) + "\'" +
                                            ",\'" + str(reservado.fecha_fin) + "\'" + 
                                            ",\'" + str(reservado.hora_inicio) + "\'" +
                                            ",\'" + str(reservado.hora_fin) + "\'" +
                                            "," + str(reservado.id_grupo) + ");"
            )

        except Exception as e:
            print(e)
            return lanzarError(str(e), 404, "Error", "about:blank")

        conex.commit()
        conex.close()

        return {"status":"Reserva realizado con éxito"}

    else:
        return lanzarError("Error", 404, "Error", "about:blank")