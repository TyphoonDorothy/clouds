DELIMITER $$

DROP PROCEDURE IF EXISTS InsertSportsmanProgram;

CREATE PROCEDURE `InsertSportsmanProgram`(
    IN `p_sportsman_id` INT,
    IN `p_program_id` INT
)
BEGIN
    DECLARE `sportsman_exists` BOOLEAN;
    DECLARE `program_exists` BOOLEAN;

    SELECT EXISTS(SELECT 1 FROM `sportsman` WHERE `id` = `p_sportsman_id`)
    INTO `sportsman_exists`;

    IF `sportsman_exists` = 0 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Sportsman ID does not exist.';
    END IF;

    SELECT EXISTS(SELECT 1 FROM `program` WHERE `id` = `p_program_id`)
    INTO `program_exists`;

    IF `program_exists` = 0 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Program ID does not exist.';
    END IF;

    INSERT INTO `sportsman_has_program` (`sportsman_id`, `program_id`)
    VALUES (`p_sportsman_id`, `p_program_id`)
    ON DUPLICATE KEY UPDATE `program_id` = `p_program_id`;
END$$

DELIMITER ;
