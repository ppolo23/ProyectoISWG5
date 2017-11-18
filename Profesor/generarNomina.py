import psycopg2
import pprint

def conexion():
    conn_string = "host='localhost' dbname='BaseDatosProfesores' user='postgres' password=''"
    # print de la conexión a realizar
    print ('Connecting to database \n	->%s ' % (conn_string))
 
    # se realiza una conexión
    conn = psycopg2.connect(conn_string)
 
    # conn.cursor devuelve un objeto cursor con el que se podrán realizar consultas
    cursor = conn.cursor()
    
    return cursor
    


def generarNominas (cursor):
    #consultas para recibir los datos del profesor(hay que añadir WHERE para especificar cual de ellos es
    cursor.execute("SELECT nombre FROM profesor")
    records = cursor.fetchone()
    nombre=" ".join(records)
    
    cursor.execute("SELECT apellido FROM profesor")
    records = cursor.fetchone()
    apellido=" ".join(records)

    cursor.execute("SELECT dni FROM profesor")
    records = cursor.fetchone()
    apellido=" ".join(records)

    cursor.execute("SELECT categoria FROM profesor")
    records = cursor.fetchone()
    apellido=" ".join(records)

    cursor.execute("SELECT antiguedad FROM profesor")
    records = cursor.fetchone()
    apellido=" ".join(records)

    cursor.execute("SELECT tramosDoc FROM profesor")
    records = cursor.fetchone()
    apellido=" ".join(records)
    
    cursor.execute("SELECT tramosInv FROM profesor")
    records = cursor.fetchone()
    apellido=" ".join(records)

    cursor.execute("SELECT nomina FROM profesor")
    records = cursor.fetchone()
    apellido=" ".join(records)

    
    #Creación y escritura del txt con los datos y nómina del profesor
    f = open ('nominas.txt','w')
    f.write('Nomina profesor\n\n')
    f.write('Nombre: \n' + nombre)
    f.write('Apellidos: \n' + apellido)
    f.write('DNI: \n' + dni )
    f.write('Categoría: \n' + categoria)
    f.write('Antigüedad: \n' + antiguedad)
    f.write('Tramos docentes: \n' + tramosDoc)
    f.write('Tramos investigación: \n' +tramosInv )
    f.write('Nómina: \n' + nomina )
    f.close()


#
cursor=conexion()
generarNominas(cursor)



