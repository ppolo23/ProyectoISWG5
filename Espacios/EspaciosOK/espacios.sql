/*
Created		02/12/2017
Modified		02/12/2017
Project		
Model		
Company		
Author		
Version		
Database		PostgreSQL 7 
*/




Create table  ESPACIOS
(
	cod_id Integer NOT NULL UNIQUE ,
	nombre Text NOT NULL UNIQUE ,
	facultad Text NOT NULL,
	tipo Text NOT NULL Check (tipo in ('laboratorio','aula','salon de actos','salon de grados')) ,
	capacidad Smallint NOT NULL,
	precioHora Integer NULL ,
 primary key (cod_id)
);

Create table  ALQUILADOS
(
	cod_id Integer NOT NULL,
	fecha Date NOT NULL,
	horaInicio Time NOT NULL,
	horaFin Time NOT NULL,
	id_prof Integer NOT NULL,
 primary key (cod_id,fecha,horaInicio)
);

Create table  RESERVADOS
(
	cod_id Integer NOT NULL,
	fechaInicio Date NOT NULL,
	diaSemana Text NOT NULL Check (diaSemana in ('Lunes','Martes','Miercoles','Jueves','Viernes')),
	fechaFin Date NOT NULL,
	horaInicio Time NOT NULL,
	horaFin Time NOT NULL,
	id_grupo Integer NOT NULL,
 primary key (cod_id,fechaInicio,diaSemana,fechaFin,horaInicio)
);


Alter table ALQUILADOS add  foreign key (cod_id) references ESPACIOS (cod_id)  on update restrict  on delete restrict ;
Alter table RESERVADOS add  foreign key (cod_id) references ESPACIOS (cod_id)  on update restrict  on delete restrict ;



