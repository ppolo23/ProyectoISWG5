/*
Created		07/11/2017
Modified		21/11/2017
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
	"fecha" Date NOT NULL,
	"correo" Text NOT NULL,
	"id" serial,
 primary key ("dni")
) Without Oids;


Create table "Asignatura"
(
	"CodAsignatura" Numeric NOT NULL UNIQUE,
	"nombre" Text NOT NULL,
	"tipo" Text NOT NULL Check (tipo in ('Obligatoria','Transversal','Optativa')),
	"creditos" Numeric NOT NULL,
	
 primary key ("CodAsignatura")
) Without Oids;


Create table "Carrera"
(
	"CodCarrera" Numeric NOT NULL UNIQUE,
	"nombre" Text NOT NULL,
	"creditosTotales" Numeric NOT NULL,
	"creditosOptativos" Numeric NOT NULL
 primary key ("CodCarrera")
) Without Oids;


Create table "Cursa"
(
	"dni" Char(9) NOT NULL,
	"CodAsignatura" Numeric NOT NULL,
	"nombreAsignatura" Text NOT NULL,
	"cursoAcademico" Text NOT NULL,
	"calificacion" Real Check (calificacion between 0 and 10),
 primary key ("dni","CodAsignatura")
) Without Oids;


Create table "Matriculado"
(
	"dni" Char(9) NOT NULL,
	"CodCarrera" Numeric NOT NULL,
	"cursoAcademico" Text NOT NULL,
	"fechaLimite" Date NOT NULL,
	"tipo_pago" Text NOT NULL Check (tipo_pago in ('uno','dos','tres')),
	"pUno" Boolean NOT NULL Default false,
	"pDos" Boolean NOT NULL Default false,
	"pTres" Boolean NOT NULL Default false,
 primary key ("dni","CodCarrera","cursoAcademico")
) Without Oids;


Create table "Pertenece_"
(
	"CodCarrera" Numeric NOT NULL,
	"CodAsignatura" Numeric NOT NULL,
 primary key ("CodCarrera","CodAsignatura")
) Without Oids;



/* Create Tab 'Others' for Selected Tables */


/* Create Indexes */



/* Create Foreign Keys */

Alter table "Cursa" add  foreign key ("dni") references "Alumno" ("dni") on update cascade on delete cascade;

Alter table "Matriculado" add  foreign key ("dni") references "Alumno" ("dni") on update cascade on delete cascade;

Alter table "Cursa" add  foreign key ("CodAsignatura") references "Asignatura" ("CodAsignatura") on update restrict on delete restrict;

Alter table "Pertenece_" add  foreign key ("CodAsignatura") references "Asignatura" ("CodAsignatura") on update restrict on delete restrict;

Alter table "Matriculado" add  foreign key ("CodCarrera") references "Carrera" ("CodCarrera") on update cascade on delete cascade;

Alter table "Pertenece_" add  foreign key ("CodCarrera") references "Carrera" ("CodCarrera") on update restrict on delete restrict;





