import connexion
import psycopg2
from swagger_server.models.alquilado import Alquilado
from swagger_server.models.espacio import Espacio
from swagger_server.models.reservado import Reservado
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime

def conectar():

    conexion = psycopg2.connect(
        database = "MyDB",
        user = "postgres",
        password = "postgres",
        host = "127.0.0.1",
        port = "5432"
    )

    return conexion

def lanzarError(msg, status, title, typee):
    """
    Lanza un mensaje de \"error\" en forma de jSon
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
    Alquila un �nico espacio mediante un registro json
    :param alquilado: Espacio que se necesita alquilar
    :type alquilado: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        alquilado = Alquilado.from_dict(connexion.request.get_json())
	
	
        conex = conectar()
        cursor = conex.cursor()
        
        num = cursor.execute(
            'SELECT COUNT(*) \
             FROM alquilados ;')
        
        cursor.execute(
            'INSERT INTO "alquilados" VALUES (espacio.cod_id,espacio.fecha,espacio.horaInicio,espacio.horaFin,espacio.id_prof)' + ";"
        )

        #rows = cursor.fetchall()  #lista de elementos que contiene la query

        num2 = cursor.execute(
            'SELECT COUNT(*) \
             FROM alquilados ;')
        
        conex.close()
    
        if num2 == num:
            return lanzarError("Problema alquilando, intentelo de nuevo", 404, "Error", "about:blank")

        else:
            return lanzarError("Espacio Alquilado correctamente!!", 200, "Genial!", "about:blank")
	
	
    return 'do some magic!'


def espacio_cod_id_get(codId):
    """
    Devuelve un espacio
    Devuelve un �nico espacio identificado por su codId de espacio
    :param codId: N�mero de identificaci�n del espacio
    :type codId: str

    :rtype: Espacio
    """
    conex = conectar()                  #conectarse a la base de datos
    cursor = conex.cursor()             #

    cursor.execute(
        "SELECT row_to_json(espacio) \
         FROM espacios \
         WHERE cod_id = " + str(codId) + ";"
    )

    rows = cursor.fetchall()

    conex.close()

    if len(rows) == 0:
        return lanzarError("Espacio no encontrado", 404, "Error", "about:blank")

    else:
        return rows[0][0]


def espacio_facultad_get(facultad):
    """
    Devuelve un espacio
    Devuelve un �nico espacio identificado por la facultad a la que pertenece
    :param facultad: facultad del espacio
    :type facultad: str

    :rtype: Espacio
    """
    conex = conectar()
    cursor = conex.cursor()

    cursor.execute(
        "SELECT array_to_json(array_agg(row_to_json(espacio))) \
         FROM espacios,alquilados,reservados \
         WHERE espacios.facultad = " + str(facultad) + " AND \
         espacios.cod_id IN (reservados OR alquilados);"
    )

    rows = cursor.fetchall()  #lista de elementos que contiene la query

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

    cursor.execute(
        "SELECT array_to_json(array_agg(row_to_json(espacio))) \
         FROM espacios,alquilados,reservados \
         WHERE espacios.cod_id IN (reservados OR alquilados);"
    )

    rows = cursor.fetchall()  #lista de elementos que contiene la query

    conex.close()

    if len(rows) == 0:
        return lanzarError("No hay espacios ocupados", 404, "Error", "about:blank")

    else:
        return rows[0][0]
#    return 'do some magic!'


def obtener_espacio():
    """
    Obtiene espacios
    Obtiene un listado de espacios del sistema.

    :rtype: List[Espacio]
    """
    conex = conectar()
    cursor = conex.cursor()

    cursor.execute(
        "SELECT array_to_json(array_agg(row_to_json(espacio))) \
         FROM espacios ;"
    )

    rows = cursor.fetchall()  #lista de elementos que contiene la query

    conex.close()

    if len(rows) == 0:
        return lanzarError("No hay espacios", 404, "Error", "about:blank")

    else:
        return rows[0][0]
    
    #return 'do some magic!'


def reserva_espacio_put(reservado):
    """
    Reservar un espacio
    Reserva un �nico espacio mediante un registro json
    :param reservado: Espacio que se necesita reservar
    :type reservado: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        reservado = Reservado.from_dict(connexion.request.get_json())

        conex = conectar()
        cursor = conex.cursor()
        
        num = cursor.execute(
            'SELECT COUNT(*) \
             FROM reservados ;')
        
        cursor.execute(
            'INSERT INTO "reservados" VALUES (espacio.cod_id,espacio.fechaInicio,espacio.diaSemana,espacio.fechaFin,espacio.horaInicio,espacio.horaFin,espacio.id_grupo)' + ";"
        )

        #rows = cursor.fetchall()  #lista de elementos que contiene la query

        num2 = cursor.execute(
            'SELECT COUNT(*) \
             FROM reservados ;')
        
        conex.close()
    
        if num2 == num:
            return lanzarError("Problema reservando, intentelo de nuevo", 404, "Error", "about:blank")

        else:
            return lanzarError("Espacio Reservado correctamente!!", 200, "Genial!", "about:blank")
		
	
    #return 'do some magic!'
