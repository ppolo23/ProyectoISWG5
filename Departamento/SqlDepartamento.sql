
Drop table "Pertenece" Restrict;
Drop table "Alumno" Restrict;
Drop table "Grupo" Restrict;
Drop table "Asignatura" Restrict;
Drop table "Departamento" Restrict;

CREATE TYPE turnoG AS ENUM ('mañana', 'tarde');
CREATE TYPE tipoG AS ENUM ('teoria','laboratorio');


Create table "Departamento"
(
	"id_departamento" Integer NOT NULL,
	"nombre" Char(20),
	"horasImpartidas" Numeric,
 primary key ("id_departamento")
) Without Oids;


Create table "Asignatura"
(
	"id_asignatura" Integer NOT NULL,
	"id_departamento" Integer NOT NULL,
	"nombre" Char(20),
 primary key ("id_asignatura","id_departamento")
) Without Oids;


Create table "Grupo"
(
	"id_grupo" Integer NOT NULL,
	"id_asignatura" Integer NOT NULL,
	"id_departamento" Integer NOT NULL,
	"turno" turnoG NOT NULL,
	"tipo" tipoG NOT NULL,
	"totalAlumnos" Integer,
	"profesor" Integer NOT NULL,
 primary key ("id_grupo","id_asignatura","id_departamento")
) Without Oids;


Create table "Alumno"
(
	"dni" Char(9) NOT NULL,
	"nombre" Char(20) NOT NULL,
 primary key ("dni")
) Without Oids;


Create table "Pertenece"
(
	"id_grupo" Integer NOT NULL,
	"id_asignatura" Integer NOT NULL,
	"id_departamento" Integer NOT NULL,
	"dni" Char(9) NOT NULL,
 primary key ("id_grupo","id_asignatura","id_departamento","dni")
) Without Oids;



Alter table "Asignatura" add  foreign key ("id_departamento") references "Departamento" ("id_departamento") on update restrict on delete restrict;

Alter table "Grupo" add  foreign key ("id_asignatura","id_departamento") references "Asignatura" ("id_asignatura","id_departamento") on update restrict on delete restrict;

Alter table "Pertenece" add  foreign key ("id_grupo","id_asignatura","id_departamento") references "Grupo" ("id_grupo","id_asignatura","id_departamento") on update restrict on delete restrict;

Alter table "Pertenece" add  foreign key ("dni") references "Alumno" ("dni") on update restrict on delete restrict;
