import connexion
import psycopg2
from time import strftime
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


def crearImpresoCobro(dni,tramo):
    impreso = open(dni + '-'+ tramo + '.txt','a')
    impreso.write('-----UNIVERSIDAD DE VILLAMAYOR-----\n')
    impreso.write('\n')
    impreso.write(dni + ' ha realizado el pago del tramo ' + tramo + 'º su matricula con éxito\n')
    impreso.write('A fecha de ' + strftime("%d/%m/%y") + '\n')
    impreso.write('\n')
    impreso.close()


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

        try:
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

            crearImpresoCobro(reservado.dni, reservado.tramo)

        except Exception as e:
            conex.close()
            print(e)
            return lanzarError(str(e), 404, "Error", "about:blank")

        return {'status':'Cobro alumno correcto'}

    else:
        lanzarError("json no válido", 404, "Error", "about:blank")


def pago_alumno(dni):
    """
    Consulta el pago del alumno
    Nos indica si el alumno ha pagado
    :param dni: El dni del alumno
    :type dni: str

    :rtype: str
    """

    try:
        conex = conectar()
        cursor = conex.cursor()

        cursor.execute(
            "SELECT row_to_json(\"CobrosMatriculas\") \
             FROM \"CobrosMatriculas\" \
             WHERE \"DNI\" = '" + str(dni) + "';"
        )

        filas = cursor.fetchall()

        conex.close()

        if len(filas) == 0:
            return lanzarError("No existe el alumno", 404, "Error", "about:blank")
        else:
            return filas[0]

    except Exception as e:
        conex.close()
        print(e)
        return lanzarError(str(e), 404, "Error", "about:blank")
