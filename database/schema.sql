CREATE TABLE IF NOT EXISTS  clerks (
   id          INT          NOT    NULL AUTO_INCREMENT,
   login       VARCHAR(16)  NOT    NULL,
   first_name  VARCHAR(45)  NOT    NULL,
   last_name   VARCHAR(45)  NOT    NULL,
   password    VARCHAR(32)  NOT    NULL,
   PRIMARY     KEY          (id),
   UNIQUE      (login));

CREATE TABLE IF NOT EXISTS customers(
    id INT NOT NULL AUTO_INCREMENT,
    email VARCHAR(255) NOT NULL,
    first_name VARCHAR(45) NOT NULL,
    last_name VARCHAR(45) NOT NULL,
    password VARCHAR(32) NOT NULL,
    address TEXT(500),
    work_phone_cc VARCHAR(4) NOT NULL,
    work_phone_number VARCHAR(255) NOT NULL,
    home_phone_cc VARCHAR(4) NOT NULL,
    home_phone_number VARCHAR(255) NOT NULL,
    PRIMARY KEY(id),
    UNIQUE(email));
