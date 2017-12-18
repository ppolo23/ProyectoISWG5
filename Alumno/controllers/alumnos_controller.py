import connexion
import psycopg2
from swagger_server.models.alumno import Alumno
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime

#Metodo para conectarnos a la base de datos alumno
def conectar():

    conexion = psycopg2.connect(dbname = 'AlumnosUniversidad',user = 'postgres', password = 'madrid9',host='localhost',port = '5433')

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
    return 'Alumno con dni: {}, ha sido borrado del sistema'.format(dni)


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

        #Insertar el registro en la tabla Alumno
        cursor.execute("INSERT INTO \"Alumno\" VALUES ("
                    + "'" + str(alumno.dni)+ "',"
                    + "'" + str(alumno.nombre) + "',"
                    + "'" + str(alumno.ape1)+ "',"
                    + "'" + str(alumno.ape2)+ "',"
                    + "'" + str(alumno.fecha)+ "',"
                    + "'" + str(alumno.correo)+ "');")
        

        #Insertar en la tabla Cursa (contiene las asignaturas que va a cursar)
        #Por cada asignatura creamos un registro con dni, codigo de la asignatura y curso academico actual

        cursoAcademico = str(datetime.now().year)+"/"+ str(datetime.now().year +1 )
        print(cursoAcademico)
        listaAsignaturas = {'Software':1,'Programacion':2,'Algoritmia':3,'Antenas':4,'Calculo':5}

        for i in range(len(alumno.asignaturas)):
            cursor.execute("INSERT INTO \"Cursa\" VALUES("
                            + "'" + str(alumno.dni)+ "',"
                            + str(listaAsignaturas[alumno.asignaturas[i]]) + ","
                            + "'" + str(cursoAcademico) + "');")
        
        
        #Creamos el registro correspondiente en la tabla Matriculado
        listaCarreras = {"Ingenieria informatica":1,"Ingenieria de telecomunicaciones":2,"Ingenieria industrial":3}
        cursor.execute("INSERT INTO \"Matriculado\"(dni,\"CodCarrera\",\"cursoAcademico\",\"fechaLimite\",tipo_pago) VALUES("
                            + "'" + str(alumno.dni)+ "',"
                            + str(listaCarreras[alumno.grado])+ ","
                            + "'" + str(cursoAcademico)+ "',"
                            + " '31/01/2017' ,"
                            + "'uno');")
        conex.commit()

        conex.close()
        return 'Alumno {} matriculado en la Universidad'.format(alumno.nombre)


def get_alumno(dni):
    """
    Devuelve un alumno.
    Devuelve el expediente de un alumno por su dni.
    :param dni: El dni del alumno
    :type dni: str

    :rtype: Alumno
    """
    conex = conectar()
    cursor = conex.cursor()

    #consulta1 = 'SELECT "Alumno".*, "Matriculado"."CodCarrera","Cursa"."CodAsignatura","Cursa"."cursoAcademico","Cursa".calificacion FROM "Alumno" WHERE dni =  \''+ dni + '\';'
    consulta = 'SELECT * FROM "Alumno" WHERE dni =  \''+ dni + '\';'

    cursor.execute(consulta)

    rows = cursor.fetchall()

    conex.close()

    if len(rows) == 0:
        return lanzarError("Alumno no encontrado", 404, "Error", "about:blank")

    else:
        return rows


def get_alumnos_por_asignatura(asignatura):
    """
    Alumnos de una asignatura.
    Devuelve los alumnos de una asignatura.
    :param asignatura: La asignatura de la Universidad
    :type asignatura: str

    :rtype: List[str]
    """
    conex = conectar()
    cursor = conex.cursor()

    cursor.execute(
        'SELECT "Alumno".nombre \
         FROM "Cursa" inner join "Alumno" on "Cursa".dni = "Alumno".dni \
         WHERE "Cursa"."CodAsignatura" =  \''+ asignatura +'\';'
    )

    rows = cursor.fetchall()

    conex.close()

    if len(rows) == 0:
        return lanzarError("No hay alumnos en esa asignatura", 404, "Error", "about:blank")

    else:
        return rows


def get_alumnos_por_carrera(carrera):
    """
    Alumnos de una carrera.
    Devuelve los alumnos de una carrera.
    :param carrera: La carrera de la Universidad
    :type carrera: str

    :rtype: List[str]
    """
    conex = conectar()
    cursor = conex.cursor()


    carreras = ["informatica","telecomunicaciones", "industrial"]
    codigo = 0

    for i in range(0,3):
        if(carreras[i] in carrera):
            codigo = i+1

    if(codigo == 0): return lanzarError("Carrera no encontrada", 404, "Error", "about:blank")

    cursor.execute(
        'SELECT "Alumno".nombre \
         FROM "Matriculado" inner join "Alumno" on "Matriculado".dni = "Alumno".dni \
         WHERE "Matriculado"."CodCarrera" =  '+ str(codigo) +';'
    )

    rows = cursor.fetchall()

    conex.close()

    if len(rows) == 0:
        return lanzarError("No hay alumnos en esa carrera", 404, "Error", "about:blank")

    else:
        return rows


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
    conex = conectar()
    cursor = conex.cursor()

    cursor.execute(
        'SELECT dni,nombre,ape1 \
         FROM "Alumno" ;'
    )

    rows = cursor.fetchall()

    conex.close()

    if len(rows) == 0:
        return lanzarError("No hay alumnos", 404, "Error", "about:blank")

    else:
        return rows
