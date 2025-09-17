DROP TRIGGER IF EXISTS enforce_doctor_exists;
DROP TRIGGER IF EXISTS  doctor_exists_update;

DELIMITER $$

CREATE TRIGGER enforce_doctor_exists
BEFORE INSERT ON doctor_schedule
FOR EACH ROW
BEGIN
    DECLARE doctor_exists INT;
    SELECT COUNT(*) INTO doctor_exists FROM doctor WHERE id = NEW.doctor_id;
    IF doctor_exists = 0 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Doctor does not exist!';
    END IF;
END$$

CREATE TRIGGER doctor_exists_update
BEFORE INSERT ON doctor_schedule
FOR EACH ROW
BEGIN
    DECLARE doctor_exists INT;
    SELECT COUNT(*) INTO doctor_exists FROM doctor WHERE id = NEW.doctor_id;
    IF doctor_exists = 0 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Doctor does not exist!';
    END IF;
END$$

DELIMITER ;
