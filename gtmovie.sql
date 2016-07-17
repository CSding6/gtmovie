CREATE TABLE Customer (
    username     VARCHAR(15)    PRIMARY KEY,
    email        VARCHAR(30)    NOT NULL    UNIQUE,
    password     VARCHAR(20)    NOT NULL
);

CREATE TABLE Manager(
    username     VARCHAR(15)    PRIMARY KEY,
    email        VARCHAR(30)    NOT NULL    UNIQUE,
    password     VARCHAR(20)    NOT NULL
);

CREATE TABLE Movie(
    title         VARCHAR(50)    PRIMARY KEY,
    genre         VARCHAR(20)    NOT NULL,
    cast          VARCHAR(250)   NOT NULL,  
    length        DOUBLE         NOT NULL,   
    rate          DOUBLE         NOT NULL,
    synopsis      VARCHAR(500)   NOT NULL,   
    release_date  DATE           NOT NULL
);

CREATE TABLE Review (
    review_ID     INT AUTO_INCREMENT   PRIMARY KEY, 
    title         VARCHAR(50)          NOT NULL,    
    comment       VARCHAR(2000)        NOT NULL,
    rating        DOUBLE               NOT NULL, 
    username      VARCHAR(15)          NOT NULL,
    FOREIGN KEY (title)    REFERENCES Movie(title),
    FOREIGN KEY (username) REFERENCES Customer(username)
);

CREATE TABLE Payment_info(
    card_num               INT             PRIMARY KEY,
    name_on_card           VARCHAR(30)     NOT NULL, 
    cvv                    INT             NOT NULL,
    saved                  BOOLEAN         NOT NULL,
    expiration_date        DATE            NOT NULL,
    username               VARCHAR(15)     NOT NULL,
    FOREIGN KEY (username) REFERENCES Customer(username)
);

CREATE TABLE Theater(
    theater_ID        INT AUTO_INCREMENT PRIMARY KEY,
    name              VARCHAR(30)    NOT NULL,
    state             VARCHAR(20)    NOT NULL,
    city              VARCHAR(20)    NOT NULL,
    street            VARCHAR(50)    NOT NULL,
    zip               INT            NOT NULL    
);

CREATE TABLE Order_info(
    order_ID                 INT            NOT NULL     AUTO_INCREMENT  PRIMARY KEY,
    status                   VARCHAR(20)    NOT NULl,
    time                     TIME           NOT NULL,
    date                     DATE           NOT NULL,
    num_of_child_ticket      INT            NOT NULL     DEFAULT 0,
    num_of_adult_ticket      INT            NOT NULL     DEFAULT 0,
    num_of_senior_ticket     INT            NOT NULL     DEFAULT 0,     
    num_of_total_ticket      INT            NOT NULL     DEFAULT 0,
    username                 VARCHAR(15)    NOT NULL, 
    card_num                 INT            NOT NULL,
    title                    VARCHAR(50)    NOT NULL,
    theater_ID               INT            NOT NULL,
    FOREIGN KEY (username)   REFERENCES Customer(username),
    FOREIGN KEY (title)      REFERENCES Movie(title),
    FOREIGN KEY (theater_ID) REFERENCES Theater(theater_ID),
    FOREIGN KEY (card_num)   REFERENCES Payment_info(card_num)
);

CREATE TABLE Plays_at(
    theater_ID    INT             NOT NULL,
    title         VARCHAR(50)     NOT NULL,
    playing       BOOLEAN         NOT NULL,
    PRIMARY KEY(theater_ID, title),
    FOREIGN KEY(theater_ID) REFERENCES Theater(theater_ID),
    FOREIGN KEY(title)      REFERENCES Movie(title)
);

CREATE TABLE Show_time(
    theater_ID    INT             NOT NULL,
    title         VARCHAR(50)     NOT NULL,
    show_time     TIMESTAMP       NOT NULL,
    PRIMARY KEY(theater_ID, title, show_time),
    FOREIGN KEY(theater_ID) REFERENCES Plays_at(theater_ID),
    FOREIGN KEY(title)      REFERENCES Plays_at(title)
);

CREATE TABLE Prefers(
    theater_ID    INT             NOT NULL,
    username      VARCHAR(15)     NOT NULL,    
    PRIMARY KEY(theater_ID, username),
    FOREIGN KEY(theater_ID) REFERENCES Theater(theater_ID),
    FOREIGN KEY(username)   REFERENCES Customer(username)
);

CREATE TABLE System_info(
    cancellation_fee       DOUBLE        NOT NULL     DEFAULT 5.0,
    senior_discount        DOUBLE        NOT NULL     DEFAULT 0.8,
    child_discount         DOUBLE        NOT NULL     DEFAULT 0.7,
    manager_password       VARCHAR(20)   NOT NULL,
    PRIMARY KEY(cancellation_fee)
);


