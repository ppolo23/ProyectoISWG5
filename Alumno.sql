/*
Created		01/11/2017
Modified		01/11/2017
Project		
Model			
Company		
Author		
Version		
Database		PostgreSQL 8.1 
*/


/* Create Domains */



/* Create Tables */


Create table "Carrera"
(
	"codCarrera" Numeric NOT NULL UNIQUE,
	"nombre" Text NOT NULL,
 primary key ("codCarrera")
) Without Oids;


Create table "Asignatura"
(
	"codAsig" Name NOT NULL UNIQUE,
	"nombre" Text NOT NULL,
	"numCreditos" Numeric NOT NULL,
	"tipo" Text NOT NULL,
 primary key ("codAsig")
) Without Oids;


Create table "Alumno"
(
	"dni" Char(9) NOT NULL UNIQUE,
	"nombre" Text NOT NULL,
	"ape1" Text NOT NULL,
	"ape2" Text,
	"fecha" Date NOT NULL,
	"direccion" Text,
	"correo" Text NOT NULL,
 primary key ("dni")
) Without Oids;


Create table "Matriculado"
(
	"dni" Char(9) NOT NULL,
	"codCarrera" Numeric NOT NULL,
	"codAsig" Name NOT NULL,
 primary key ("dni","codCarrera","codAsig")
) Without Oids;



/* Create Foreign Keys */

Alter table "Matriculado" add  foreign key ("codCarrera") references "Carrera" ("codCarrera") on update restrict on delete restrict;

Alter table "Matriculado" add  foreign key ("codAsig") references "Asignatura" ("codAsig") on update restrict on delete restrict;

Alter table "Matriculado" add  foreign key ("dni") references "Alumno" ("dni") on update restrict on delete restrict;





