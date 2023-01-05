CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
USE hbnb_dev_db;
GRANT ALL PRIVELEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
USE performance_schema;
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;
SET FOREIGN_KEY_CHECKS=1;