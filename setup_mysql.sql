CREATE DATABASE IF NOT EXISTS incometracker;
CREATE USER IF NOT EXISTS 'root'@'localhost' IDENTIFIED BY 'root';
GRANT ALL PRIVILEGES ON `incometracker`.* TO 'root'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'root'@'localhost';
FLUSH PRIVILEGES;

CREATE TABLE users(
    id INT(11),
    username varchar(32),
    email varchar(30),
    password varchar(60),
    primary key(id)
    );
