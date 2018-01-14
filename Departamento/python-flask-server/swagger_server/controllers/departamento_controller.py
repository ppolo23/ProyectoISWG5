import connexion
import psycopg2
from swagger_server.models.alumno import Alumno
from swagger_server.models.departamento import Departamento
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime


def conectar():

    conexion = psycopg2.connect(dbname = 'Departamento',user = 'postgres', password = 'madrid9',host='localhost',port = '5433')

    return conexion

def lanzarError(msg, status, title, typee):
    """
    Lanza un mensaje de \"error\" en forma de json
    """
    d = {}
    d["detail"] = msg
    d["error"] = status
    d["title"] = title
    d["type"] = typee
    return d


def asignar_grupo(alumno):
    """
    Asigna grupo al alumno
    Recibe datos alumno y le asigna un grupo de una asignatura determinada
    :param alumno: Datos del alumno y asignatura a matricular
    :type alumno: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        alumno = Alumno.from_dict(connexion.request.get_json())

        conex = conectar()
        cursor = conex.cursor()

        cursor.execute('Select dni from "Alumno" where dni =\''+ alumno.dni +'\';')
        al = cursor.fetchall()

        if(len(al) == 0):
                #Insertamos los datos del alumno en la tabla Alumno
                cursor.execute('Insert into "Alumno" values(\''+str(alumno.dni)+'\' , \''+str(alumno.nombre)+ '\');')

        #Insertar datos en tabla Grupo: primero ver el grupo que le corresponde y despues insertar los datos

        #Para comprobar la cantidad de alumnos de esa asignatura
        consulta1 = 'Select "totalAlumnos" from "Grupo" where id_asignatura ='+str(alumno.id_asignatura)+';'
        
        #Para ver a que departamento pertenece la asignatura
        consulta2 = 'Select id_departamento from "Asignatura" where id_asignatura='+str(alumno.id_asignatura)+';'

        cursor.execute(consulta1)
        numAlumnos = cursor.fetchall()

        cursor.execute(consulta2)
        dep = cursor.fetchall()


        if(len(numAlumnos) == 0):
            grupo = 1
            turno = "mañana"
            #Creamos un nuevo grupo
            cursor.execute("INSERT INTO \"Grupo\" VALUES ("
                    + str(grupo) + ","
                    + str(alumno.id_asignatura) + ","
                    + str(dep[0][0])+ ","
                    + "'" + str(turno)+ "',"
                    + "'" + "teoria" + "',"
                    + "'" + str(1)+ "',"
                    + str(1) +");")

        elif(numAlumnos[0][0] == 50):
            grupo = 2
            turno = 'tarde'
            #Creamos un nuevo grupo
            cursor.execute("INSERT INTO \"Grupo\" VALUES ("
                    + str(grupo) + ","
                    + str(alumno.id_asignatura) + ","
                    + str(dep[0][0])+ ","
                    + "'" + str(turno)+ "',"
                    + "'" + "teoria" + "',"
                    + "'" + str(1)+ "',"
                    + str(1) +");")
        else:
            if(numAlumnos[0][0] <= 50):
                #Actualizar grupo 1
                grupo = 1
                cursor.execute("UPDATE \"Grupo\""
                +"SET \"totalAlumnos\" ="+str(numAlumnos[0][0]+1)
                +"WHERE id_asignatura = "+str(alumno.id_asignatura)+" AND id_grupo = 1;")

            else:
                #Actualizar grupo 2
                grupo = 2
                cursor.execute("UPDATE \"Grupo\""
                +"SET \"totalAlumnos\" ="+str(numAlumnos[0][0]+1)
                +"WHERE id_asignatura = "+str(alumno.id_asignatura)+" AND id_grupo = 2;")

        #Insertar datos en la tabla Pertenece
        cursor.execute("INSERT INTO \"Pertenece\" VALUES("
                + str(grupo) +","
                + str(alumno.id_asignatura) +","
                + str(dep[0][0]) +","
                +"'"+ str(alumno.dni) +"');")

        conex.commit()
        conex.close()

        return 'Grupo {} asignado al alumno'.format(grupo)
    else:
        return 'No se ha podido asignar un grupo'


def borrar_departamento(codID):
    """
    elimina un departamento
    elimina un departamento de la lista
    :param codID: Código de identificación del departamento a eliminar
    :type codID: str

    :rtype: None
    """
    conex = conectar()
    cursor = conex.cursor()

    cursor.execute(
        "DELETE \
         FROM Departamento \
         WHERE id_departamento = " + str(codID) + ";"
    )

    rows = cursor.fetchall()

    conex.commit()
    conex.close()

    return 'Alumno con dni: {}, ha sido borrado del sistema'.format(dni)


def crear_departamento(departamento):
    """
    Crea un departamento
    Añade un departamento a la lista de departamentos
    :param departamento: El departamento que se va a añadir.
    :type departamento: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        departamento = Departamento.from_dict(connexion.request.get_json())

        conex = conectar()
        cursor = conex.cursor()

        cursor.execute("INSERT INTO \"Departamento\" VALUES ("
                    + "'" + str(departamento.id_departamento)+ "',"
                    + "'" + str(departamento.nombre) + "',"
                    + "'" + str(departamento.horasImpartidas)+"');")
        
        
        asignaturasUni=["Software","Programacion","Algoritmia"]
        for i in range(0,len(asignaturasUni)):
            consulta = ' INSERT INTO "Asignatura" VALUES (\'' + str(asignaturasUni[i]) + '\' ;'
            cursor.execute(consulta)

        conex.commit()

    return 'Departamento creado.'


def departamento_cod_id_get(codID):
    """
    Devuelve un departamento
    Devuelve un único departamento identificado por su código de identificación
    :param codID: Número de identificación del departamento
    :type codID: str

    :rtype: Departamento
    """
    conex = conectar()
    cursor = conex.cursor()

    cursor.execute(
        "SELECT row_to_json(Departamento) \
         FROM Departamento \
         WHERE id_departamento = " + str(codID) + ";"
    )

    rows = cursor.fetchall()

    conex.close()

    if len(rows) == 0:
        return lanzarError("Departamento no encontrado", 404, "Error", "about:blank")

    else:
        return rows[0][0]



def get_asignaturas_departamento(codID):
    """
    Asignaturas de un departamento
    Devuelve lista con las asignaturas impartidas por el departamento
    :param codID: Código de identificación del departamento que imparte dichas asignaturas
    :type codID: str

    :rtype: List[Departamento]
    """
    conex = conectar()
    cursor = conex.cursor()

    cursor.execute(
        "SELECT array_to_json(array_agg(row_to_json(t))) \
         FROM (SELECT row_to_json(Asignatura.nombre) \
         FROM Departamento, Asignatura \
         WHERE Asignatura.id_departamento = " + str(codID) + "AND Asignatura.id_departamento = Departamento.id_departamento) as t;"
    )

    rows = cursor.fetchall()

    conex.close()

    if len(rows) == 0:
        return lanzarError("Departamento no encontrado", 404, "Error", "about:blank")

    else:
        return rows[0][0]


def obtener_departamento(tamagnoPagina=None, numeroPagina=None):
    """
    Obtiene los departamentos
    Obtiene un listado de los departamentos existentes en el sistema
    :param tamagnoPagina: número de departamentos devueltos
    :type tamagnoPagina: int
    :param numeroPagina: número de páginas devueltas
    :type numeroPagina: int

    :rtype: List[Departamento]
    """
    conex = conectar()
    cursor = conex.cursor()

    cursor.execute(
        'SELECT  id_departamento, nombre, "horasImpartidas"\
         FROM "Departamento" ;'
    )

    rows = cursor.fetchall()

    conex.close()

    if len(rows) == 0:
        return lanzarError("No hay departamentos", 404, "Error", "about:blank")

    else:
        return rows
