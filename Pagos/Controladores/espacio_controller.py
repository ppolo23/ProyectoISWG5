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

        return 'Cobro espacio correcto'


def pago_espacio(id_espacio):
    """
    Consulta pago/alquiler espacio.
    Indica si el espacio ha sido pagado
    :param id_espacio: El identificador del espacio
    :type id_espacio: int

    :rtype: Espacio
    """
    return 'do some magic!'
