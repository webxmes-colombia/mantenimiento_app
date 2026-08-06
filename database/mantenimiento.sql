-- =====================================================
-- ELIMINAR Y CREAR LA BASE DE DATOS
-- =====================================================

DROP DATABASE IF EXISTS mantenimiento_db;

CREATE DATABASE mantenimiento_db
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;

USE mantenimiento_db;

-- =====================================================
-- TABLA USUARIOS
-- =====================================================

CREATE TABLE IF NOT EXISTS usuarios (

    id INT NOT NULL AUTO_INCREMENT,

    nombre VARCHAR(100) NOT NULL,

    email VARCHAR(100) NOT NULL UNIQUE,

    password VARCHAR(255) NOT NULL,

    rol ENUM('admin','tecnico') NOT NULL,

    creado_en TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    PRIMARY KEY (id)

);

-- =====================================================
-- USUARIOS DE PRUEBA
-- =====================================================

INSERT INTO usuarios
(nombre,email,password,rol)
VALUES

('Cesar Molina',
'admin@empresa.com',
'Admin123',
'admin'),

('Ana Gomez',
'ana@empresa.com',
'Tecnico123',
'tecnico'),

('Luis Martinez',
'luis@empresa.com',
'Tecnico123',
'tecnico'),

('Sofia Lopez',
'sofia@empresa.com',
'Tecnico123',
'tecnico'),

('Jorge Ramirez',
'jorge@empresa.com',
'Admin123',
'admin');

-- =====================================================
-- TABLA CLIENTES
-- =====================================================

CREATE TABLE IF NOT EXISTS clientes (

    id INT NOT NULL AUTO_INCREMENT,

    nombre VARCHAR(100) NOT NULL,

    empresa VARCHAR(100) NOT NULL,

    direccion VARCHAR(200) NOT NULL,

    telefono VARCHAR(20) NOT NULL,

    email VARCHAR(100) NOT NULL,

    creado_en TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    PRIMARY KEY (id)

);

-- =====================================================
-- CLIENTES DE PRUEBA
-- =====================================================

INSERT INTO clientes
(nombre,empresa,direccion,telefono,email)
VALUES

(
'Roberto Silva',
'TechCorp Solutions',
'Chapinero Alto',
'3105595301',
'roberto@techcorp.com'
),

(
'Maria Torres',
'Innovatech',
'Calle 45 #89-98',
'3118120925',
'mtorres@innovatech.com'
),

(
'David Guzman',
'Logística Express',
'Industrial Park Bodega 4',
'3158120329',
'dguzman@logexpress.com'
),

(
'Elena Rostova',
'Rostova Legal',
'Edificio Torres Plaza 5B',
'6012053294',
'elena@rostovalegal.com'
),

(
'Gabriel Fernandez',
'Estudio Creativo',
'Av. Primavera 404',
'6012134713',
'gabriel@estudiocreativo.com'
);


-- =====================================================
-- TABLA EQUIPOS
-- =====================================================

CREATE TABLE IF NOT EXISTS equipos (

    id INT NOT NULL AUTO_INCREMENT,

    cliente_id INT NOT NULL,

    marca VARCHAR(50) NOT NULL,

    modelo VARCHAR(100) NOT NULL,

    procesador VARCHAR(100) NOT NULL,

    ram VARCHAR(20) NOT NULL,

    disco VARCHAR(20) NOT NULL,

    tipo_disco ENUM('HDD','SSD','NVMe') NOT NULL,

    estado ENUM('Bueno','Regular','Critico') NOT NULL,

    creado_en TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    PRIMARY KEY(id),

    CONSTRAINT fk_cliente
        FOREIGN KEY(cliente_id)
        REFERENCES clientes(id)
        ON DELETE CASCADE

);

-- =====================================================
-- EQUIPOS DE PRUEBA
-- =====================================================

INSERT INTO equipos
(cliente_id,marca,modelo,procesador,ram,disco,tipo_disco,estado)
VALUES

(1,'Dell','Latitude 5420','Intel Core i7-1185G7','16 GB','512 GB','NVMe','Bueno'),

(2,'HP','ProBook 450 G8','Intel Core i5-1135G7','8 GB','256 GB','SSD','Regular'),

(3,'Lenovo','ThinkPad T14','AMD Ryzen 7 PRO 4750U','32 GB','1 TB','NVMe','Bueno'),

(4,'Apple','MacBook Pro 14','Apple M1 Pro','16 GB','512 GB','SSD','Critico'),

(5,'ASUS','ROG Strix G15','AMD Ryzen 9 5900HX','32 GB','1 TB','NVMe','Regular');


-- =====================================================
-- TABLA MANTENIMIENTOS
-- =====================================================

CREATE TABLE IF NOT EXISTS mantenimientos (

    id INT NOT NULL AUTO_INCREMENT,

    equipo_id INT NOT NULL,

    tecnico_id INT NOT NULL,

    errores_encontrados TEXT NOT NULL,

    solucion_detallada TEXT NOT NULL,

    recomendaciones TEXT,

    fecha_mantenimiento DATE NOT NULL,

    proximo_mantenimiento DATE NOT NULL,

    creado_en TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    PRIMARY KEY(id),

    CONSTRAINT fk_equipo
        FOREIGN KEY(equipo_id)
        REFERENCES equipos(id)
        ON DELETE CASCADE,

    CONSTRAINT fk_tecnico
        FOREIGN KEY(tecnico_id)
        REFERENCES usuarios(id)
        ON DELETE CASCADE

);

-- =====================================================
-- TABLA EVIDENCIAS
-- =====================================================

CREATE TABLE IF NOT EXISTS evidencias (

    id INT NOT NULL AUTO_INCREMENT,

    mantenimiento_id INT NOT NULL,

    nombre_archivo VARCHAR(255) NOT NULL,

    ruta_archivo VARCHAR(255) NOT NULL,

    tipo_archivo ENUM('imagen','video') NOT NULL,

    etapa ENUM('antes','durante','despues') NOT NULL,

    creado_en TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    PRIMARY KEY(id),

    CONSTRAINT fk_mantenimiento
        FOREIGN KEY(mantenimiento_id)
        REFERENCES mantenimientos(id)
        ON DELETE CASCADE

);
-- =====================================================
-- TABLA AUDITORIA
-- =====================================================

CREATE TABLE IF NOT EXISTS auditoria (

    id INT NOT NULL AUTO_INCREMENT,

    usuario_id INT NOT NULL,

    modulo VARCHAR(50) NOT NULL,

    accion VARCHAR(50) NOT NULL,

    descripcion TEXT,

    ip VARCHAR(45),

    fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    PRIMARY KEY(id),

    CONSTRAINT fk_usuario_auditoria
        FOREIGN KEY(usuario_id)
        REFERENCES usuarios(id)
        ON DELETE CASCADE

);