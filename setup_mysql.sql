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

CREATE TABLE houses(
    houseId INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    location VARCHAR(255) NOT NULL,
    unitCount INT NOT NULL,
    occupancyRate DECIMAL(5, 2),
    totalRent DECIMAL(10, 2) NOT NULL
);

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
