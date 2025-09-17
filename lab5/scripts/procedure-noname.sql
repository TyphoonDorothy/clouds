DELIMITER $$

DROP PROCEDURE IF EXISTS InsertNonameRows;

CREATE PROCEDURE InsertNonameRows()
BEGIN
    DECLARE i INT DEFAULT 1;
    DECLARE last_id INT;

    WHILE i <= 10 DO
        INSERT INTO sportsman (name, surname, age, height, weight)
        VALUES ('Placeholder', 'Placeholder', 100, 123, 123);

        SET last_id = LAST_INSERT_ID();

        UPDATE sportsman
        SET name = CONCAT('Noname', last_id)
        WHERE id = last_id;

        SET i = i + 1;
    END WHILE;
END $$

DELIMITER ;
