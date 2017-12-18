/* Create Domains */
Create domain "tramos" Char(1) Check(1,2,3);

/* Create Tables */

Create table "CobrosMatriculas"
(
	"DNI" Char(9) NOT NULL UNIQUE,
	"fecha_limite" Date NOT NULL,
	"tramo" "tramos" NOT NULL,
	"pagado" Boolean NOT NULL,
 primary key ("DNI")
) Without Oids;

