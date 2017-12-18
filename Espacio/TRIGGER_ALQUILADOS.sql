﻿CREATE OR REPLACE FUNCTION comprobarHora2()
RETURNS TRIGGER AS $TRIGGERCOMPROBAR2$
BEGIN
	IF(NEW.horafin > NEW.horainicio) THEN
		RETURN NEW;
	ELSE
		RAISE EXCEPTION 'La hora de fin es incorrecta, debe ser posterior a la de inicio';
		RETURN OLD;
	END IF;
END;
$TRIGGERCOMPROBAR2$
LANGUAGE 'plpgsql';
CREATE TRIGGER TRIGGERCOMPROBAR2
BEFORE INSERT ON "alquilados"
FOR EACH ROW EXECUTE PROCEDURE comprobarHora2();
