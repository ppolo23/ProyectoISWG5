
DROP TYPE "tramos" Restrict;
DROP TABLE "CobrosEspacios" Restrict;
DROP TABLE "NominasProfesores" Restrict;
DROP TABLE "CobrosMatriculas" Restrict;


CREATE TYPE tramos AS ENUM ('1','2','3');

CREATE TABLE "CobrosMatriculas"
(
	"DNI" Char(9) NOT NULL UNIQUE,
	"fecha_limite" Date NOT NULL,
	"tramo" tramos NOT NULL,
	"pagado" Boolean NOT NULL,
 PRIMARY KEY ("DNI")
) Without Oids;


CREATE TABLE "NominasProfesores"
(
	"DNI" Char(9) NOT NULL UNIQUE,
	"cantidad" Numeric(10,3) NOT NULL,
	"fecha" Date NOT NULL,
 PRIMARY KEY ("DNI")
) Without Oids;


CREATE TABLE "CobrosEspacios"
(
	"cod_id" Integer NOT NULL,
	"fecha" Date NOT NULL,
	"hora" Time NOT NULL,
	"id_prof" Integer,
	"cantidad" Real,
 PRIMARY KEY ("cod_id","fecha","hora")
) Without Oids;
