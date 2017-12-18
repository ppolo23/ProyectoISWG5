## ProyectoISWG5




![Alt text](./modelo.png)

#### Objetos:
- *API REST* del módulo Alumno
- Base datos Alumno/Matricula
- *API REST* del módulo Espacio
- Base datos Espacio
- *API REST* del módulo Pagos
- *API REST* del módulo Departamento
- *API REST* del módulo Profesor

### Dependencias
- Toad Data Modeler para visualizar el modelado de la bases de datos.
- PostgreSQL
- Python Flask
- Módulo psycog2 (interfaz PostgreSQL - Pyhton)
- Cualquier editor de texto valdrá para visualizar el contenido de las APIs

#### Instalar:
1. Crear una base de datos en PostgreSQL con el esquema el del archivo `Alumnos.sql`
2. Generación del servidor flask correspondiente al microservico Alumno mediante API Alumno especificada en fichero `APIAlumno.yaml`
3. Sustitución de los archivos generados automáticamente en la carpeta controllers por los ficheros `alumnos_controller.py`, `asignaturas_controller.py`, `carreras_controller.py`

4. Crear una base de datos en PostgreSQL con el esquema el del archivo `Espacios.sql`
5.Generación del servidor flask correspondiente al microservico Espacios mediante API Espacio especificada en fichero `APIEspacio.yaml`
6. Sustitución de los archivos generados automáticamente en la carpeta controllers por el fichero `espacios_controller.py`
