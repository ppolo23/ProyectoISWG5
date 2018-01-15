import connexion
import psycopg2
from swagger_server.models.alumno import Alumno
from swagger_server.models.matricula import Matricula
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime

apiBase = "http://localhost:8080/dep/"
headers = {'Authorization': 'Bearer ', "Content-Type": "application/json", "data":"data"}

# Metodo para conectarnos a la base de datos alumno
def conectar():

    conexion = psycopg2.connect(
        dbname = 'Universidad',
        user = 'postgres',
        password = 'madrid9',
        host='localhost',
        port = '5433'
    )

    return conexion

# Metodo para lanzar los errores
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
    try:
        conex = conectar()
        cursor = conex.cursor()

        consulta = 'DELETE FROM "Alumno" WHERE dni = \'' + dni + '\' ;'
        cursor.execute(consulta)

        conex.commit()
        conex.close()

        return {'status':'Alumno con dni: {}, ha sido borrado del sistema'.format(dni)}

    except Exception as e:
        conex.close()
        print(e)
        return lanzarError(str(e), 404, "Error", "about:blank")


#Se crean tantos registros como asignaturas tenga el alumno (ARREGLARLO)
def get_alumno(dni):
    """
    Devuelve un alumno.
    Devuelve el expediente de un alumno por su dni.
    :param dni: El dni del alumno
    :type dni: str

    :rtype: Alumno
    """
    try:
        conex = conectar()
        cursor = conex.cursor()

        consulta = 'SELECT "Alumno".*, "Cursa".* \
                    FROM "Cursa" inner join "Alumno" on "Cursa".dni = "Alumno".dni \
                    WHERE "Alumno".dni =  \''+ dni + '\';'

        cursor.execute(consulta)
        rows = cursor.fetchall()
        conex.close()

        if len(rows) == 0:
            return lanzarError("Alumno no encontrado", 404, "Error", "about:blank")
        else:
            return rows

    except Exception as e:
        conex.close()
        print(e)
        return lanzarError(str(e), 404, "Error", "about:blank")


def get_alumnos_por_asignatura(asignatura):
    """
    Alumnos de una asignatura.
    Devuelve los alumnos de una asignatura.
    :param asignatura: La asignatura de la Universidad
    :type asignatura: str

    :rtype: List[str]
    """
    try:
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

    except Exception as e:
        conex.close()
        print(e)
        return lanzarError(str(e), 404, "Error", "about:blank")


def get_alumnos_por_carrera(carrera):
    """
    Alumnos de una carrera.
    Devuelve los alumnos de una carrera.
    :param carrera: La carrera de la Universidad
    :type carrera: str

    :rtype: List[str]
    """
    try:
        conex = conectar()
        cursor = conex.cursor()

        carreras = ["informatica","industrial"]
        codigo = 0

        for i in range(0,2):
            if (carreras[i] in carrera):
                codigo = i+1

        if (codigo == 0):
            return lanzarError("Carrera no encontrada", 404, "Error", "about:blank")

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

    except Exception as e:
        conex.close()
        print(e)
        return lanzarError(str(e), 404, "Error", "about:blank")


def matricula(matricula):
    """
    Matriculacion del alumno
    Matriculacion del alumno en las asignaturas indicadas
    :param matricula: Los datos de la matricula.
    :type matricula: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:

        matricula = Matricula.from_dict(connexion.request.get_json())

        try:
            cursoAcademico = str(datetime.now().year) + "/" + str(datetime.now().year + 1)
            credCurso = 60
            
            conex = conectar()
            cursor = conex.cursor()

            # Sacamos los creditos optativos que tiene la carrera
            cursor.execute('Select "creditosOptativos" from "Carrera" where "nombre" = (select grado from "Alumno" where id = \'' + str(matricula.id_alumno) + '\');')
            credOptativos = cursor.fetchall()

            credCurso = credCurso + (0.10 * int(credOptativos[0][0]))
            creds = 0

            # Calculamos el numero de creditos de los que se quiere matricular el alumno
            for i in range(0, len(matricula.asignaturas)):
                cursor.execute('Select creditos from "Asignatura" where "CodAsignatura" ='+ str(matricula.asignaturas[i]) +';')
                credAsig = cursor.fetchall()
                creds+= int(credAsig[0][0])

            # Si el numero de creditos es mayor que el 10% de los creditos optativos del plan de estudios no se puede
            if (creds > credCurso):
                return {'status':'No se puede matricular de tantas asignaturas'}

            # Comprobamos si el alumno ha realizado la reserva
            cursor.execute('Select * from "Alumno" where id =\'' + str(matricula.id_alumno)+'\';')
            alumno = cursor.fetchall()

            if (alumno[0] == None):
                return {'status':'No ha efecutado la reserva de la matricula'}
        
            asignaturasUni = ["Software","Programacion","Algoritmia"]

            # Insertamos un registro por cada asignatura en Cursa
            for i in range(0, len(matricula.asignaturas)):
                consulta = 'INSERT INTO "Cursa" VALUES (\''+ str(alumno[0][0]) + '\' , \'' + str(matricula.asignaturas[i]) + '\' , \'' + str(asignaturasUni[matricula.asignaturas[i]-1]) +  '\',\''+str(cursoAcademico)+'\');'
                cursor.execute(consulta)

            # Creamos el registro correspondiente en la tabla Matriculado
            listaCarreras = {
                "Ingenieria informatica":1,
                "Ingenieria de telecomunicaciones":2,
                "Ingenieria industrial":3
            }

            cursor.execute(
                "INSERT INTO \"Matriculado\"(dni,\"CodCarrera\",\"cursoAcademico\",\"fechaLimite\",tipo_pago) VALUES("
                + "'" + str(alumno[0][0])+ "',"
                + str(listaCarreras[alumno[0][6]])+ ","
                + "'" + str(cursoAcademico) + "',"
                + " '31/01/2018' ," + "'" 
                + matricula.plazo + "');"
            )

            conex.commit()

            #Realizamos la llamada a la operacion de Departamento en su servidor propio para enviarle los datos que necesita
            for i in range (len(matricula.asignaturas)):
                datos = {

                    "dni": str(alumno[0][0]),
                    "nombre": str(alumno[0][1]),
                    "id_asignatura": matricula.asignaturas[i],
                    "nombreAsignatura": str(asignaturasUni[matricula.asignaturas[i]-1])
                }
                r = requests.post(apiBase + "asignarGrupo", data=json.dumps(datos), headers=headers)

            return {'status':'Matricula efectuada {}'.format(matricula.id_alumno)}

        except Exception as e:
            conex.close()
            print(e)
            return lanzarError(str(e), 404, "Error", "about:blank")

    else:
        lanzarError("json no válido", 404, "Error", "about:blank")


def obtener_alumnos():
    """
    Obtiene los alumnos
    Obtiene un listado de alumnos del sistema.
    :param tamanoPagina: Número de alumnos devueltas
    :type tamanoPagina: int
    :param numeroPaginas: Número de páginas devueltas
    :type numeroPaginas: int

    :rtype: List[Alumno]
    """
    try:
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

    except Exception as e:
        conex.close()
        print(e)
        return lanzarError(str(e), 404, "Error", "about:blank")


def reserva(alumno):
    """
    Reserva la matricula de un alumno
    Se efectua la reserva de la matricula de un alumno
    :param alumno: el alumno que reserva
    :type alumno: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:

        alumno = Alumno.from_dict(connexion.request.get_json())

        try:
            conex = conectar()
            cursor = conex.cursor()

            # Si el alumno ya se encuentra matriculado o ha efectuado la reserva
            cursor.execute(
                'SELECT * \
                 FROM "Alumno" \
                 WHERE dni = \''+ str(alumno.dni) + '\';'
            )

            id = cursor.fetchall()

            if (len(id) != 0):
                return {'status':'El alumno ya se encuentra matriculado'}

            # Añadir a tabla columna grado, establecer en swagger enum de grado

            # Insertar el registro en la tabla Alumno
            cursor.execute(
                "INSERT INTO \"Alumno\" VALUES ("
                    + "'" + str(alumno.dni) + "',"
                    + "'" + str(alumno.nombre) + "',"
                    + "'" + str(alumno.ape1) + "',"
                    + "'" + str(alumno.ape2) + "',"
                    + "'" + str(alumno.fecha) + "',"
                    + "'" + str(alumno.correo) + "',"
                    + "'" + str(alumno.grado) + "');"
            )

            conex.commit()

            # Obtenemos el codigo de identificacion que se le ha asignado
            cursor.execute(
                'SELECT id \
                 FROM "Alumno" \
                 WHERE dni = \''+ str(alumno.dni) + '\';'
            )

            codigo = cursor.fetchall()
            conex.close()

            return {'status':'Reserva realizada. Codigo de identificación: {}'.format(codigo[0][0])}

        except Exception as e:
            conex.close()
            print(e)
            return lanzarError(str(e), 404, "Error", "about:blank")

    else:
        lanzarError("json no válido", 404, "Error", "about:blank")