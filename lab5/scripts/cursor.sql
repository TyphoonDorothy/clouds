DELIMITER //

DROP PROCEDURE IF EXISTS GenerateDatabasesAndTables;

CREATE PROCEDURE GenerateDatabasesAndTables()
BEGIN
    DECLARE done INT DEFAULT 0;
    DECLARE db_name VARCHAR(100);
    DECLARE table_count INT;
    DECLARE table_name VARCHAR(100);
    DECLARE column_count INT;
    DECLARE column_name VARCHAR(64);
    DECLARE column_type VARCHAR(20);
    DECLARE i INT;
    DECLARE j INT;

    DECLARE db_cursor CURSOR FOR SELECT name FROM doctor;
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = 1;

    OPEN db_cursor;

    db_loop: LOOP
        FETCH db_cursor INTO db_name;
        IF done THEN
            LEAVE db_loop;
        END IF;

        SET @new_db_name = CONCAT('`', db_name, '`');
        
        SET @create_db_stmt = CONCAT('CREATE DATABASE IF NOT EXISTS ', @new_db_name);
        PREPARE stmt_db FROM @create_db_stmt;
        EXECUTE stmt_db;
        DEALLOCATE PREPARE stmt_db;

        SET table_count = FLOOR(1 + (RAND() * 9));
        
        SET i = 1;
        WHILE i <= table_count DO
            SET table_name = CONCAT(@new_db_name, '.', '`', db_name, '_', i, '`');
            
            SET @drop_table_stmt = CONCAT('DROP TABLE IF EXISTS ', table_name);
            PREPARE stmt_drop_table FROM @drop_table_stmt;
            EXECUTE stmt_drop_table;
            DEALLOCATE PREPARE stmt_drop_table;
            
            SET column_count = FLOOR(1 + (RAND() * 5));
            
            SET @create_table_stmt = CONCAT('CREATE TABLE ', table_name, ' (');
            
            SET j = 1;
            WHILE j <= column_count DO
                SET column_name = CONCAT('col_', j);

                CASE FLOOR(1 + (RAND() * 3))
                    WHEN 1 THEN SET column_type = 'VARCHAR(50)';
                    WHEN 2 THEN SET column_type = 'INT';
                    WHEN 3 THEN SET column_type = 'DATE';
                END CASE;

                SET @create_table_stmt = CONCAT(@create_table_stmt, column_name, ' ', column_type);

                IF j < column_count THEN
                    SET @create_table_stmt = CONCAT(@create_table_stmt, ', ');
                ELSE
                    SET @create_table_stmt = CONCAT(@create_table_stmt, ');');  -- Close the create statement
                END IF;

                SET j = j + 1;
            END WHILE;

            PREPARE stmt_create_table FROM @create_table_stmt;
            EXECUTE stmt_create_table;
            DEALLOCATE PREPARE stmt_create_table;

            SET i = i + 1;
        END WHILE;
    END LOOP;

    CLOSE db_cursor;
END //

DELIMITER ;
