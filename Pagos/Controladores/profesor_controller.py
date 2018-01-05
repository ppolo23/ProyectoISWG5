import connexion
import psycopg2
from swagger_server.models.profesor import Profesor
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

def cobro_nomina(dni):
    """
    Consulta pago nomina
    Indica si el profesor ha cobrado su nomina
    :param dni: El dni del profesor
    :type dni: str

    :rtype: str
    """
    return 'do some magic!'


def insertar_nomina_profesor(reservado):
    """
    Insertar registro de nomina profesor
    Insertar registro de nomina profesor
    :param reservado: Nomina que ha sido cobrada
    :type reservado: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        reservado = Profesor.from_dict(connexion.request.get_json())

        conex = conectar()
        cursor = conex.cursor()

        cursor.execute(
        "INSERT INTO \"NominasProfesores\" VALUES (\'" + str(reservado.dni) + "\'" +
                                                   "," + str(reservado.cantidad) +
                                                 ",\'" + str(reservado.fecha) + "\'" + ");"
        )

        conex.commit()
        conex.close()

        return 'Nomina profesor registrada'
