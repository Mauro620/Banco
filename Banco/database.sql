CREATE DATABASE IF NOT EXISTS banco;
use banco;

CREATE TABLE usuario(
id          int(25) not null,
saldo       float(12) DEFAULT 0.0,
nombre      varchar(100),
apellidos   varchar(100),
email       varchar(100) not null,
passwd      varchar(100) not null,
fecha       date not null,
CONSTRAINT pk_usuarios PRIMARY KEY(email),
CONSTRAINT uq_email UNIQUE(email)
)ENGINE=InnoDb;

CREATE TABLE transaction(
reference       int(25) auto_increment not null,
saldo           float(12) not null default 0.0,
remitente       varchar(100),
destiny         varchar(100) not null,
descripcion     MEDIUMTEXT,
fecha           date not null,
CONSTRAINT pk_transactions PRIMARY KEY(reference),
CONSTRAINT fk_remitente FOREIGN KEY (remitente) REFERENCES usuario(email)         
)ENGINE=InnoDb;
