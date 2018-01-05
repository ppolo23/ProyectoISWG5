import connexion
import psycopg2
from swagger_server.models.alumno import Alumno
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

def insertar_cobro_matricula(reservado):
    """
    Insertar registro de cobro de matricula
    Inserta registro de cobro de matricula
    :param reservado: Espacio que se necesita reservar
    :type reservado: dict | bytes

    :rtype: None
    """

    if connexion.request.is_json:
        reservado = Alumno.from_dict(connexion.request.get_json())

        conex = conectar()
        cursor = conex.cursor()

        cursor.execute(
        "INSERT INTO \"CobrosMatriculas\" VALUES (" + str(reservado.dni) +
                                        ",\'" + str(reservado.fecha_limite) + "\'" +
                                        ",\'" + str(reservado.tramo) + "\'" +
                                        "," + str(reservado.pagado) + ");"
        )

        conex.commit()
        conex.close()

        return 'Cobro alumno correcto'


def pago_alumno(dni):
    """
    Consulta el pago del alumno
    Nos indica si el alumno ha pagado
    :param dni: El dni del alumno
    :type dni: str

    :rtype: str
    """
    return 'do some magic!'
