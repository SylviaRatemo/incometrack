CREATE DATABASE IF NOT EXISTS incometracker;
CREATE USER IF NOT EXISTS 'root'@'localhost' IDENTIFIED BY 'root';
GRANT ALL PRIVILEGES ON `incometracker`.* TO 'root'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'root'@'localhost';
FLUSH PRIVILEGES;

setup issues:
ALTER USER 'root'@'localhost' IDENTIFIED WITH 'mysql_native_password' BY 'root';

CREATE TABLE users(
    id INT AUTO_INCREMENT PRIMARY KEY,
    username varchar(32),
    email varchar(30),
    password varchar(60)
    );
INSERT INTO users (username, email, password)
VALUES ('Sylvia Ratemo', 'ratemosylvia@gmail.com', 'root');


CREATE TABLE houses(
    houseId INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    location VARCHAR(255) NOT NULL,
    unitCount INT NOT NULL,
    occupancyRate DECIMAL(5, 2) DEFAULT NULL,
    totalRent DECIMAL(10, 2) NOT NULL
);
INSERT INTO houses (name, location, unitCount, occupancyRate, totalRent)
VALUES ('Bluehouse', 'Githurai 45', 35, 80.2, 110000), 
('House 2', 'Githurai 45', 34, 90, 71700);

CREATE TABLE units(
    unitId VARCHAR(30),
    houseId INT,
    tenantId INT DEFAULT NULL,
    meterNo INT,
    description VARCHAR(255),
    status BOOLEAN,
    PRIMARY KEY (unitId, houseId),
    FOREIGN KEY (houseId) REFERENCES houses (houseId)
);
--FOREIGN KEY (tenantId) REFERENCES tenants (tenantId)
--ALTER TABLE units ADD CONSTRAINT fk_tenantId FOREIGN KEY (tenantId) REFERENCES tenants (tenantId);

CREATE TABLE tenants(
    tenantId INT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    IdNumber INT NOT NULL,
    unitId VARCHAR(30),
    rentId INT,
    FOREIGN KEY (unitId) REFERENCES units (unitId),
    FOREIGN KEY (rentId) REFERENCES rent (rentId)
);

CREATE TABLE rent(
    rentId INT PRIMARY KEY,
    unitId VARCHAR(30),
    amount INT NOT NULL,
    status BOOLEAN,
    FOREIGN KEY (unitId) REFERENCES units (unitId)
);

--occupancy rate computation
UPDATE houses as h
SET h.occupancyRate = (
    SELECT houseId, COUNT(unitId)
    FROM units
    GROUP BY houseId
);
