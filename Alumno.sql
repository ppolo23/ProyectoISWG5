/*
Created		07/11/2017
Modified		13/11/2017
Project		
Model			
Company		
Author		
Version		
Database		PostgreSQL 8.1 
*/


/* Create Domains */



/* Create Tables */


Create table "Alumno"
(
	"dni" Char(9) NOT NULL UNIQUE,
	"nombre" Text NOT NULL,
	"ape1" Text NOT NULL,
	"ape2" Text,
	"fecha" Date,
	"direccion" Text,
	"correo" Text NOT NULL,
 primary key ("dni")
) Without Oids;


Create table "Asignatura"
(
	"CodAsignatura" Numeric NOT NULL UNIQUE,
	"CodCarrera" Numeric NOT NULL,
	"nombre" Text NOT NULL,
	"tipo" Text NOT NULL Check (tipo in ('Obligatoria','Transversal','Optativa')),
	"creditos" Numeric NOT NULL,
 primary key ("CodAsignatura","CodCarrera")
) Without Oids;


Create table "Carrera"
(
	"CodCarrera" Numeric NOT NULL UNIQUE,
 primary key ("CodCarrera")
) Without Oids;


Create table "Cursa"
(
	"dni" Char(9) NOT NULL,
	"CodAsignatura" Numeric NOT NULL,
	"CodCarrera" Numeric NOT NULL,
 primary key ("dni","CodAsignatura","CodCarrera")
) Without Oids;


Create table "Matriculado"
(
	"dni" Char(9) NOT NULL,
	"CodCarrera" Numeric NOT NULL,
 primary key ("dni","CodCarrera")
) Without Oids;



/* Create Tab 'Others' for Selected Tables */


/* Create Indexes */



/* Create Foreign Keys */

Alter table "Cursa" add  foreign key ("dni") references "Alumno" ("dni") on update restrict on delete restrict;

Alter table "Matriculado" add  foreign key ("dni") references "Alumno" ("dni") on update restrict on delete restrict;

Alter table "Cursa" add  foreign key ("CodAsignatura","CodCarrera") references "Asignatura" ("CodAsignatura","CodCarrera") on update restrict on delete restrict;

Alter table "Asignatura" add  foreign key ("CodCarrera") references "Carrera" ("CodCarrera") on update restrict on delete restrict;

Alter table "Matriculado" add  foreign key ("CodCarrera") references "Carrera" ("CodCarrera") on update restrict on delete restrict;





