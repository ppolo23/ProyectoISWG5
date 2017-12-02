import connexion
import psycopg2
from swagger_server.models.alumno import Alumno
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime

#Metodo para conectarnos a la base de datos alumno
def conectar():

    conexion = psycopg2.connect(dbname = 'Universidad',user = 'postgres', password = 'madrid9',host='localhost',port = '5433')

    return conexion

#Metodo para lanzar los errores
def lanzarError(msg, status, title, typee):
    d = {}
    d["detail"] = msg
    d["error"] = status
    d["title"] = title
    d["type"] = typee
    return d

def borrar_alumno(dni):
    """
    elimina un alumno
    elimina un alumno de la lista
    :param dni: dni del alumno a eliminar
    :type dni: str

    :rtype: None
    """
    consulta = 'DELETE FROM "Alumno" WHERE dni = \''+dni+'\' ;'
    conex = conectar()
    cursor = conex.cursor()

    cursor.execute(consulta)

    conex.commit()
    conex.close()

    #·return 'do some magic!'


def crear_alumno(alumno):
    """
    Crea un alumno
    Añade un alumno a la lista.
    :param alumno: El alumno que se va a añadir.
    :type alumno: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        alumno = Alumno.from_dict(connexion.request.get_json())

        conex = conectar()
        cursor = conex.cursor()
        #Primero insertamos los datos del alumno en la tabla Alumno si no habia estado matriculado en un año anterior
        cursor.execute(
        'SELECT row_to_json(dni) \
         FROM "Alumno" \
         WHERE dni =  \''+ dni + '\';'
        )

        rows = cursor.fetchall()

        if len(rows) == 0:
            consulta = 'INSERT INTO "Alumno" VALUES ( \''+ alumno.dni + '\' , \'' + alumno.nombre + '\',\'' + 
                                                alumno.ape1 +'\' , \'' + alumno.ape2 + '\' , \''+ alumno.fecha 
                                                + '\', \'' +alumno.correo +'\','+ 0 +', ' + 0 +','+ 0');'
            cursor.execute(consulta)

    #Despues cogemos las asignaturas de las que se ha matriculado, y por cada una se crea un registro en la tabla Curso
        asignaturas[] = alumno.asignaturas
        curso = datetime.datetime.now()
        cAcademico1 = curso.year
        cAcademico2 = cAcademico+1

        for i in range(0,len(asignaturas)-1):
            consulta = ' INSERT INTO "Cursa" VALUES (\''+ alumno.dni + '\' , \'' + asignaturas[i].codigo + '\',\''+str(cAcademico1)+"/"+str(cAcademico2) +'\');'
            cursor.execute(consulta)

        consulta = ' INSERT INTO "Matriculado" VALUES (\''+ alumno.dni + '\' , \'' + alumno.grado + '\',\''+str(cAcademico1)+"/"+str(cAcademico2) +'\');'
        cursor.execute(consulta)

        conex.commit()
        conex.close()

    return "Inserción del alumno {} realizada con exito".format(alumno.dni)

def get_alumno(dni):
    """
    Devuelve expediente alumno.
    Devuelve el expediente de alumno utilizando el dni.
    :param dni: El dni del alumno
    :type dni: str

    :rtype: Alumno
    """
    conex = conectar()
    cursor = conex.cursor()

    cursor.execute(
        'SELECT row_to_json(dni) \
         FROM "Alumno" \
         WHERE dni =  \''+ dni + '\';'
    )

    rows = cursor.fetchall()

    conex.close()

    if len(rows) == 0:
        return lanzarError("Alumno no encontrado", 404, "Error", "about:blank")

    else:
        return row_to_json(rows)


def get_alumnos_por_asignatura(asignatura):
    """
    Alumnos de una asignatura.
    Devuelve los alumnos de una asignatura.
    :param asignatura: La asignatura de la Universidad
    :type asignatura: str

    :rtype: List[Alumno]
    """
    conex = conectar()
    cursor = conex.cursor()

    cursor.execute(
        'SELECT row_to_json(dni) \
         FROM "Cursa" \
         WHERE asignatura =  \''+ asignatura +'\';'
    )

    rows = cursor.fetchall()

    conex.close()

    if len(rows) == 0:
        return lanzarError("No hay alumnos en esa asignatura", 404, "Error", "about:blank")

    else:
        return row_to_json(rows)


def get_alumnos_por_carrera(carrera):
    """
    Alumnos de una carrera.
    Devuelve los alumnos de una carrera.
    :param carrera: La carrera de la Universidad
    :type carrera: str

    :rtype: List[Alumno]
    """
    conex = conectar()
    cursor = conex.cursor()

    cursor.execute(
        'SELECT row_to_json(dni) \
         FROM "Matriculado" \
         WHERE carrera =  \''+ carrera +'\';'
    )

    rows = cursor.fetchall()

    conex.close()

    if len(rows) == 0:
        return lanzarError("No hay alumnos en esa asignatura", 404, "Error", "about:blank")

    else:
        return row_to_json(rows)


def obtener_alumnos(tamanoPagina=None, numeroPaginas=None):
    """
    Obtiene los alumnos
    Obtiene un listado de alumnos del sistema.
    :param tamanoPagina: Número de alumnos devueltas
    :type tamanoPagina: int
    :param numeroPaginas: Número de páginas devueltas
    :type numeroPaginas: int

    :rtype: List[Alumno]
    """
    return 'do some magic!'
