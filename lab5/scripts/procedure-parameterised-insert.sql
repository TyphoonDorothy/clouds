DELIMITER $$

DROP PROCEDURE IF EXISTS InsertDish;

CREATE PROCEDURE InsertDish(
    IN name_param VARCHAR(255),
    IN calories_param DECIMAL(9, 6)
)
BEGIN
    INSERT INTO dish (
        name,
        calories
    )
    VALUES (
        name_param,
        calories_param
    );
END$$

DELIMITER ;