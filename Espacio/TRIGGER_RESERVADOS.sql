CREATE OR REPLACE FUNCTION comprobarHora()
RETURNS TRIGGER AS $TRIGGERCOMPROBAR$
BEGIN
	IF(NEW.horafin < NEW.horainicio)THEN
		RAISE EXCEPTION 'La hora de fin es incorrecta, debe ser posterior a la de inicio';
		RETURN OLD;

	ELSIF (NEW.fechafin < NEW.fechainicio) THEN
		RAISE EXCEPTION 'La fecha de fin es incorrecta, debe ser posterior a la de inicio';
		RETURN OLD;

	ELSE
		RETURN NEW;
		
	END IF;
END;
$TRIGGERCOMPROBAR$
LANGUAGE 'plpgsql';
CREATE TRIGGER TRIGGERCOMPROBAR
BEFORE INSERT ON "reservados"
FOR EACH ROW EXECUTE PROCEDURE comprobarHora();
