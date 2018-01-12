import connexion
import psycopg2
from swagger_server.models.espacio import Espacio
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime

def conectar():
    conexion = psycopg2.connect(
        database = "Pagos",
        user = "postgres",
        password = "postgres",
        host = "127.0.0.1",
        port = "5432"
    )
    return conexion

def lanzarError(msg, status, title, typee):
    """
    Lanza un mensaje de "error" en forma de json
    """
    d = {}
    d["detail"] = msg
    d["error"] = status
    d["title"] = title
    d["type"] = typee
    return d

def insertar_cobro_espacio(reservado):
    """
    Insertar registro de cobro de espacio
    Insertar registro de cobro de espacio
    :param reservado: Nomina que ha sido cobrada
    :type reservado: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        reservado = Espacio.from_dict(connexion.request.get_json())

        try:
            conex = conectar()
            cursor = conex.cursor()

            cursor.execute(
                "INSERT INTO \"CobrosEspacios\" VALUES (" + str(reservado.cod_id) +
                            ",\'" + str(reservado.fecha) + "\'" +
                            ",\'" + str(reservado.hora) + "\'" +
                            "," + str(reservado.id_prof) +
                            "," + str(reservado.cantidad) + ");"
            )

            conex.commit()
            conex.close()

            return {'status':'Cobro espacio correcto'}

        except Exception as e:
            conex.close()
            print(e)
            return lanzarError(str(e), 404, "Error", "about:blank")

    else:
        lanzarError("json no válido", 404, "Error", "about:blank")


def pago_espacio(id_espacio):
    """
    Consulta pago/alquiler espacio.
    Indica si el espacio ha sido pagado
    :param id_espacio: El identificador del espacio
    :type id_espacio: int

    :rtype: Espacio
    """

    try:
        conex = conectar()
        cursor = conex.cursor()

        cursor.execute(
            "SELECT row_to_json(\"CobrosEspacios\") \
             FROM \"CobrosEspacios\" \
             WHERE cod_id = " + str(id_espacio) + ";"
        )

        filas = cursor.fetchall()

        conex.close()

        if len(filas) == 0:
            return lanzarError("No existe el espacio", 404, "Error", "about:blank")
        else:
            return filas[0]

    except Exception as e:
        conex.close()
        print(e)
        return lanzarError(str(e), 404, "Error", "about:blank")