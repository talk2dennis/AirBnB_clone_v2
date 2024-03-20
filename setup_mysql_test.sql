-- script that prepares a MySQL server for the project
-- A database hbnb_test_db
-- A new user hbnb_test (in localhost)
-- The password of hbnb_test should be set to hbnb_test_pwd

CREATE DATABASE IF NOT EXISTS `hbnb_test_db`;

CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';

FLUSH PRIVILEGES;

GRANT SELECT ON `performance_schema`.* TO 'hbnb_test'@'localhost'
