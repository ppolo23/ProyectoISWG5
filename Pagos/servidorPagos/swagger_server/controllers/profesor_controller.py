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

def cobro_nomina(dni):
    """
    Consulta pago nomina
    Indica si el profesor ha cobrado su nomina
    :param dni: El dni del profesor
    :type dni: str

    :rtype: str
    """

    try:
        conex = conectar()
        cursor = conex.cursor()

        cursor.execute(
            "SELECT row_to_json(\"NominasProfesores\") \
             FROM \"NominasProfesores\" \
             WHERE \"DNI\" = '" + str(dni) + "';"
        )

        filas = cursor.fetchall()

        conex.close()

        if len(filas) == 0:
            return lanzarError("No existe la nomina profesor", 404, "Error", "about:blank")
        else:
            return filas[0]

    except Exception as e:
        conex.close()
        print(e)
        return lanzarError(str(e), 404, "Error", "about:blank")


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

        try:
            conex = conectar()
            cursor = conex.cursor()

            cursor.execute(
                "INSERT INTO \"NominasProfesores\" VALUES (\'" + str(reservado.dni) + "\'" +
                            "," + str(reservado.cantidad) +
                            ",\'" + str(reservado.fecha) + "\'" + ");"
            )

            conex.commit()
            conex.close()

        except Exception as e:
            conex.close()
            print(e)
            return lanzarError(str(e), 404, "Error", "about:blank")

        return {'status':'Nomina profesor registrada'}

    else:
        lanzarError("json no válido", 404, "Error", "about:blank")
