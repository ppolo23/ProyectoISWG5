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

### Puertos:
- 5000 - Alumno
- 6000 - Pagos
- 7000 - Espacios
- 8080 - Departamento

#### Uso:
1. Crear una base de datos en PostgreSQL con el esquema el del archivo `Alumnos.sql` y con el nombre 'AlumnosUniversidad'
2. Una vez instalados tanto Python Flask como psycog2, ejecutar el siguiente comando en la consola del sistema en la carpeta python-flask-server y ejecutar los comandos 'pip install -r requirements.txt' y 'py -m swagger_server', en ese orden.
3. Tras ejecutar el ultimo comando, el servidor estará activo. Ir a 'http://localhost:8080/apiAlumno/ui/' para visualizar las operaciones sobre alumnos disponibles.

4. Crear una base de datos en PostgreSQL con el esquema el del archivo `Espacios.sql` 
5. Abrir una consola del sistema en la ruta de la carpeta del python-flask-server correspondiente a Espacios y ejecutar de nuevo los comandos mencionados en el apartado 2.
6. Una vez el servidor esté activo, ir a 'http://localhost:8080/APIespacios/ui/' para visualizar las operaciones sobre espacios disponibles.
