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
		database = "espacios",
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
	Alquila un ?nico espacio mediante un registro json
	:param alquilado: Espacio que se necesita alquilar
	:type alquilado: dict | bytes

	:rtype: None
	"""
	if connexion.request.is_json:
		alquilado = Alquilado.from_dict(connexion.request.get_json())

		print(alquilado)
	
		conex = conectar()
		cursor = conex.cursor()

		try:
			cursor.execute(
			"INSERT INTO alquilados VALUES (" + str(alquilado.cod_id) +
											",\'" + str(alquilado.fecha) + "\'" +
											",\'" + str(alquilado.hora_inicio) + "\'" +
											",\'" + str(alquilado.hora_fin) + "\'" + 
											"," + str(alquilado.id_prof) + ");")
		except Exception as e:
			return e

		conex.commit()
		conex.close()

	return "Reserva correcta"

def espacio_cod_id_get(codId):
	"""
	Devuelve un espacio
	Devuelve un ?nico espacio identificado por su codId de espacio
	:param codId: N?mero de identificaci?n del espacio
	:type codId: str
	:rtype: Espacio
	"""

	conex = conectar()
	cursor = conex.cursor()

	cursor.execute(
		"SELECT row_to_json(espacios) \
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
	Devuelve un ?nico espacio identificado por la facultad a la que pertenece
	:param facultad: facultad del espacio
	:type facultad: str

	:rtype: Espacio
	"""
	conex = conectar()
	cursor = conex.cursor()

	cursor.execute(
		"SELECT array_to_json(array_agg(row_to_json(espacios))) \
		 FROM \"espacios\" \
		 WHERE espacios.facultad = '" + str(facultad) + "';"
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
	   "SELECT array_to_json(array_agg(row_to_json(t)))\
		FROM (SELECT espacios.cod_id, espacios.nombre, espacios.facultad, tipo, capacidad, preciohora\
		FROM espacios, reservados, alquilados\
		WHERE espacios.cod_id = reservados.cod_id OR espacios.cod_id = alquilados.cod_id) as t;"
		)

	rows = cursor.fetchall()  #lista de elementos que contiene la query

	conex.close()

	if len(rows) == 0:
		return lanzarError("No hay espacios ocupados", 404, "Error", "about:blank")

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

	cursor.execute(
		"SELECT array_to_json(array_agg(row_to_json(espacios))) \
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
	Reserva un ?nico espacio mediante un registro json
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
			"INSERT INTO alquilados VALUES (" + str(reservado.cod_id) +
											",\'" + str(reservado.fechaInicio) + "\'" +
											",\'" + str(reservado.diaSemana) + "\'" +
											",\'" + str(reservado.fechaFin) + "\'" + 
											",\'" + str(reservado.horaInicio) + "\'" +
											",\'" + str(reservado.horaFin) + "\'" +
											"," + str(reservado.id_grupo) + ");"
			)
		except Exception as e:
			return e

		conex.commit()
		conex.close()

		return "Reserva correcta"

	else:
		return "Peto json"
