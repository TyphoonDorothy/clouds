DELIMITER //

DROP TRIGGER IF EXISTS validate_calories_not_ending_in_double_zero;
DROP TRIGGER IF EXISTS validate_calories_update_not_ending_in_double_zero;

CREATE TRIGGER validate_calories_not_ending_in_double_zero
BEFORE INSERT ON ingredient
FOR EACH ROW
BEGIN
    IF NEW.calories LIKE '%00' THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'The calories column value cannot end with two zeros.';
    END IF;
END //

CREATE TRIGGER validate_calories_update_not_ending_in_double_zero
BEFORE UPDATE ON ingredient
FOR EACH ROW
BEGIN
    IF NEW.calories LIKE '%00' THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'The cakiries column value cannot end with two zeros.';
    END IF;
END //

DELIMITER ;
