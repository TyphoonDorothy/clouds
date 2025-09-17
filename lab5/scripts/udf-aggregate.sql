DELIMITER $$

CREATE PROCEDURE AggregateColumn(
    IN table_name VARCHAR(255),
    IN column_name VARCHAR(255),
    IN operation VARCHAR(10),
    OUT result DECIMAL(18, 2)
) 
BEGIN
    SET @query = CONCAT('SELECT ', operation, '(', column_name, ') INTO @output FROM ', table_name);
    PREPARE stmt FROM @query;
    EXECUTE stmt;
    DEALLOCATE PREPARE stmt;

    SET result = @output;
END$$

DELIMITER ;
