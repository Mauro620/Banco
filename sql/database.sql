CREATE DATABASE IF NOT EXISTS veterinaria;
use veterinaria;

CREATE TABLE mascotas(
id          int(25) not null auto_increment,
nombre      varchar(100) not null,
especie   varchar(100) not null,
raza       varchar(100) not null,
color      varchar(100) not null,
peso        int(10) not null,
altura        int(10) not null,
estado      varchar(25),
birthday    date not null,
fecha       date not null,
CONSTRAINT pk_mascotas PRIMARY KEY(id)
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