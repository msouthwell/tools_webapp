CREATE TABLE IF NOT EXISTS  clerks (
   clerk_id          INT                      NOT NULL AUTO_INCREMENT,
   login       VARCHAR(16)              NOT NULL,
   first_name  VARCHAR(45)              NOT NULL,
   last_name   VARCHAR(45)              NOT NULL,
   password    VARCHAR(32)              NOT NULL,
   PRIMARY KEY (clerk_id),
   UNIQUE      (login));

CREATE TABLE IF NOT EXISTS customers(
    customer_id                  INT             NOT NULL AUTO_INCREMENT,
    email               VARCHAR(255)    NOT NULL,
    first_name          VARCHAR(45)     NOT NULL,
    last_name           VARCHAR(45)     NOT NULL,
    password            VARCHAR(32)     NOT NULL,
    address             TEXT(500),
    work_phone_cc       VARCHAR(4)      NOT NULL,
    work_phone_number   VARCHAR(255)    NOT NULL,
    home_phone_cc       VARCHAR(4)      NOT NULL,
    home_phone_number   VARCHAR(255)    NOT NULL,
    PRIMARY KEY (customer_id),
    UNIQUE      (email));
    
CREATE TABLE IF NOT EXISTS reservations(
    reservation_id                  INT             NOT NULL AUTO_INCREMENT,
    start_date          DATE            NOT NULL,
    end_date            DATE            NOT NULL,
    customer_id         INT             NOT NULL,
    clerk_id_pickup     INT,
    clerk_id_dropoff    INT,
    credit_card         VARCHAR(45),
    expiration_date     DATE,
    PRIMARY KEY (reservation_id),
    UNIQUE (customer_id, credit_card),
    FOREIGN KEY (customer_id)           REFERENCES customers (customer_id),
    FOREIGN KEY (clerk_id_pickup)       REFERENCES clerks (clerk_id),
    FOREIGN KEY (clerk_id_dropoff)      REFERENCES clerks (clerk_id) );
    
CREATE TABLE IF NOT EXISTS categories(
    category_id                  INT             NOT NULL AUTO_INCREMENT,
    category            VARCHAR(255)    NOT NULL,
    has_accessories     BOOLEAN         NOT NULL,
    PRIMARY KEY (category_id), 
    UNIQUE (category) );

CREATE TABLE IF NOT EXISTS tools( 
    tool_id                  INT             NOT NULL AUTO_INCREMENT,
    short_description   VARCHAR(255)    NOT NULL,
    full_description    TEXT(500)       NOT NULL,
    deposit             DECIMAL(7,2)    NOT NULL,
    day_price           DECIMAL(7,2)    NOT NULL,
    original_price      DECIMAL(7,2)    NOT NULL,
    category_id         INT             NOT NULL,
    PRIMARY KEY (tool_id),
    FOREIGN KEY (category_id)           REFERENCES categories (category_id) );

CREATE TABLE IF NOT EXISTS tool_accessories(
    tool_id             INT             NOT NULL,
    description         VARCHAR(255)    NOT NULL,
    PRIMARY KEY (tool_id, description),
    FOREIGN KEY (tool_id)               REFERENCES tools (tool_id) );

CREATE TABLE IF NOT EXISTS reservations_tools(
    reservation_id      INT             NOT NULL,
    tool_id             INT             NOT NULL,
    PRIMARY KEY (reservation_id, tool_id),
    FOREIGN KEY (reservation_id)        REFERENCES reservations (reservation_id),
    FOREIGN KEY (tool_id)               REFERENCES tools (tool_id) );

CREATE TABLE IF NOT EXISTS service_orders(
    service_order_id                  INT             NOT NULL AUTO_INCREMENT,
    clerk_id            INT             NOT NULL,
    tool_id             INT             NOT NULL,
    start_date          DATE            NOT NULL,
    end_date            DATE,
    est_cost            DECIMAL(7,2),
    PRIMARY KEY (service_order_id),
    FOREIGN KEY (clerk_id)              REFERENCES clerks (clerk_id),
    FOREIGN KEY (tool_id)               REFERENCES tools (tool_id) );

CREATE TABLE IF NOT EXISTS sells(
    tool_id             INT             NOT NULL,
    clerk_id            INT             NOT NULL,
    sale_date           DATE            NOT NULL,
    PRIMARY KEY (tool_id),
    FOREIGN KEY (clerk_id)              REFERENCES clerks (clerk_id),
    FOREIGN KEY (tool_id)               REFERENCES tools (tool_id) );


