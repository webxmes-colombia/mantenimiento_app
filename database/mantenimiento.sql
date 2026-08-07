-- ================================================================
-- Base de datos: mantenimiento_db
-- Proyecto Flask / MySQL para gestion de mantenimientos tecnologicos
-- Archivo autocontenido: puede importarse directamente en MySQL 8.0+
-- ================================================================

DROP DATABASE IF EXISTS mantenimiento_db;
CREATE DATABASE mantenimiento_db
  CHARACTER SET utf8mb4
  COLLATE utf8mb4_unicode_ci;

USE mantenimiento_db;

-- ----------------------------------------------------------------
-- Usuarios del sistema
-- Las contraseñas se almacenan como hashes bcrypt (nunca en texto plano).
-- Sustituya estos hashes por los generados por su aplicacion al crear usuarios reales.
-- ----------------------------------------------------------------
CREATE TABLE usuarios (
    id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(120) NOT NULL,
    correo VARCHAR(150) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    rol ENUM('Administrador', 'Tecnico', 'Consulta') NOT NULL DEFAULT 'Consulta',
    activo TINYINT(1) NOT NULL DEFAULT 1,
    fecha_creacion DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    fecha_actualizacion DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB;

CREATE TABLE clientes (
    id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(150) NOT NULL,
    nit VARCHAR(30) NOT NULL UNIQUE,
    contacto VARCHAR(120) NOT NULL,
    telefono VARCHAR(30),
    correo VARCHAR(150),
    direccion VARCHAR(200),
    ciudad VARCHAR(100),
    activo TINYINT(1) NOT NULL DEFAULT 1,
    fecha_creacion DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    fecha_actualizacion DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB;

-- Inventario y ficha taecnica de equipos
CREATE TABLE equipos (
    id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    cliente_id INT UNSIGNED NOT NULL,
    tipo VARCHAR(80) NOT NULL,
    marca VARCHAR(80) NOT NULL,
    modelo VARCHAR(120) NOT NULL,
    serial VARCHAR(120) NOT NULL UNIQUE,
    activo_fijo VARCHAR(80) UNIQUE,
    nombre_equipo VARCHAR(120) NOT NULL,
    ubicacion VARCHAR(150) NOT NULL,
    direccion_ip VARCHAR(45),
    procesador VARCHAR(150),
    ram VARCHAR(50),
    tipo_ram VARCHAR(50),
    disco VARCHAR(80),
    tipo_disco ENUM('HDD', 'SSD', 'NVMe', 'eMMC', 'Hibrido', 'No aplica') NOT NULL DEFAULT 'No aplica',
    sistema_operativo VARCHAR(120),
    antivirus ENUM('Windows Defender', 'ESET', 'Kaspersky', 'Avast', 'McAfee', 'Ninguno', 'Otro') NOT NULL DEFAULT 'Ninguno',
    estado ENUM('Operativo', 'En mantenimiento', 'Fuera de servicio', 'En reparacion', 'Baja') NOT NULL DEFAULT 'Operativo',
    accesorios TEXT,
    observaciones TEXT,
    fecha_ingreso DATE NOT NULL,
    activo ENUM('SI', 'NO') NOT NULL DEFAULT 'SI',
    fecha_creacion DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    fecha_actualizacion DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    CONSTRAINT fk_equipos_cliente
        FOREIGN KEY (cliente_id) REFERENCES clientes(id)
        ON UPDATE CASCADE ON DELETE RESTRICT,
    INDEX idx_equipos_cliente (cliente_id),
    INDEX idx_equipos_estado (estado),
    INDEX idx_equipos_activo (activo)
) ENGINE=InnoDB;

-- Historial de mantenimientos y lista de verificaciones
CREATE TABLE mantenimientos (
    id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    equipo_id INT UNSIGNED NOT NULL,
    tecnico_id INT UNSIGNED NOT NULL,
    tipo_mantenimiento ENUM('Preventivo', 'Correctivo', 'Predictivo', 'Instalacion', 'Diagnostico') NOT NULL,
    fecha_programada DATE NULL,
    fecha_mantenimiento DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    fecha_finalizacion DATETIME NULL,
    estado ENUM('Programado', 'En proceso', 'Completado', 'Cancelado') NOT NULL DEFAULT 'Programado',
    diagnostico TEXT NOT NULL,
    trabajo_realizado TEXT,
    repuestos_utilizados TEXT,
    limpieza_realizada TINYINT(1) NOT NULL DEFAULT 0,
    pasta_termica_aplicada TINYINT(1) NOT NULL DEFAULT 0,
    antivirus_actualizado TINYINT(1) NOT NULL DEFAULT 0,
    sistema_actualizado TINYINT(1) NOT NULL DEFAULT 0,
    respaldo_verificado TINYINT(1) NOT NULL DEFAULT 0,
    pruebas_funcionamiento TINYINT(1) NOT NULL DEFAULT 0,
    observaciones TEXT,
    costo DECIMAL(12,2) NOT NULL DEFAULT 0.00,
    fecha_creacion DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    fecha_actualizacion DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    CONSTRAINT fk_mantenimientos_equipo
        FOREIGN KEY (equipo_id) REFERENCES equipos(id)
        ON UPDATE CASCADE ON DELETE RESTRICT,
    CONSTRAINT fk_mantenimientos_tecnico
        FOREIGN KEY (tecnico_id) REFERENCES usuarios(id)
        ON UPDATE CASCADE ON DELETE RESTRICT,
    INDEX idx_mantenimientos_equipo (equipo_id),
    INDEX idx_mantenimientos_tecnico (tecnico_id),
    INDEX idx_mantenimientos_fecha (fecha_mantenimiento),
    INDEX idx_mantenimientos_estado (estado)
) ENGINE=InnoDB;

-- Fotografias, facturas o documentos asociados a un mantenimiento
CREATE TABLE evidencias (
    id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    mantenimiento_id INT UNSIGNED NOT NULL,
    nombre_archivo VARCHAR(255) NOT NULL,
    ruta_archivo VARCHAR(500) NOT NULL,
    tipo_archivo VARCHAR(100),
    descripcion VARCHAR(500),
    fecha_carga DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_evidencias_mantenimiento
        FOREIGN KEY (mantenimiento_id) REFERENCES mantenimientos(id)
        ON UPDATE CASCADE ON DELETE CASCADE,
    INDEX idx_evidencias_mantenimiento (mantenimiento_id)
) ENGINE=InnoDB;

-- Trazabilidad de las acciones realizadas en la aplicacion
CREATE TABLE auditoria (
    id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    usuario_id INT UNSIGNED NULL,
    accion VARCHAR(100) NOT NULL,
    entidad VARCHAR(100) NOT NULL,
    entidad_id INT UNSIGNED NULL,
    detalle TEXT,
    direccion_ip VARCHAR(45),
    fecha_registro DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_auditoria_usuario
        FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
        ON UPDATE CASCADE ON DELETE SET NULL,
    INDEX idx_auditoria_usuario (usuario_id),
    INDEX idx_auditoria_entidad (entidad, entidad_id),
    INDEX idx_auditoria_fecha (fecha_registro)
) ENGINE=InnoDB;

-- ----------------------------------------------------------------
-- Datos iniciales
-- ----------------------------------------------------------------
INSERT INTO usuarios (id, nombre, correo, password_hash, rol, activo) VALUES
    (1, 'Cesar Martinez', 'admin@empresa.com', 'scrypt:32768:8:1$C5TOPxqNXD5rGbIL$443bb11d941697e17337af318c6acfb97c519719a5fd5d5203e2203c6e549745cdd08945dff0da7d6bcc96cbee084cba80800facb3489f259d3ca02162923428', 'Administrador', 1),
    (2, 'Carlos Ramirez', 'carlos.ramirez@mantenimiento.local', '$2b$12$OqnyNmfV8hN2yfnycp1p7ewhgBfYHEEBP/T1EE7SdyWgSvMO4zmfC', 'Tecnico', 1),
    (3, 'Laura Gomez', 'laura.gomez@mantenimiento.local', '$2b$12$OqnyNmfV8hN2yfnycp1p7ewhgBfYHEEBP/T1EE7SdyWgSvMO4zmfC', 'Tecnico', 1),
    (4, 'Miguel angel Ruiz', 'miguel.ruiz@mantenimiento.local', '$2b$12$OqnyNmfV8hN2yfnycp1p7ewhgBfYHEEBP/T1EE7SdyWgSvMO4zmfC', 'Tecnico', 1),
    (5, 'Sofia Mendoza', 'sofia.mendoza@mantenimiento.local', '$2b$12$OqnyNmfV8hN2yfnycp1p7ewhgBfYHEEBP/T1EE7SdyWgSvMO4zmfC', 'Consulta', 1);

INSERT INTO clientes (id, nombre, nit, contacto, telefono, correo, direccion, ciudad) VALUES
    (1, 'Soluciones Andinas S.A.S.', '901234567-1', 'Diana Pardo', '3005550101', 'diana.pardo@andinas.com', 'Carrera 7 # 72-41', 'Bogota'),
    (2, 'Clinica San Rafael', '900456789-2', 'Jorge Cardenas', '3005550102', 'sistemas@clinicasanrafael.com', 'Calle 127 # 18-65', 'Bogota'),
    (3, 'Colegio Nuevo Horizonte', '800123456-3', 'Paola Rios', '3005550103', 'tecnologia@nuevohorizonte.edu.co', 'Avenida 19 # 110-12', 'Bogota'),
    (4, 'Logistica del Caribe Ltda.', '901678234-4', 'Andres Salas', '3005550104', 'andres.salas@logisticacaribe.com', 'Zona Industrial Mamonal, Bodega 12', 'Cartagena'),
    (5, 'Consultores Financieros G&A', '900987654-5', 'Natalia Velez', '3005550105', 'n.velez@gyaconsultores.com', 'Calle 10 # 34-20', 'Medellin');

INSERT INTO equipos
    (id, cliente_id, tipo, marca, modelo, serial, activo_fijo, nombre_equipo, ubicacion, direccion_ip, procesador, ram, tipo_ram, disco, tipo_disco, sistema_operativo, antivirus, estado, accesorios, observaciones, fecha_ingreso, activo)
VALUES
    (1, 1, 'Portatil', 'Dell', 'Latitude 5420', 'DL5420-8K7P1', 'AF-AND-001', 'AND-GERENCIA-01', 'Gerencia general', '192.168.10.21', 'Intel Core i7-1185G7', '16 GB', 'DDR4', '512 GB', 'NVMe', 'Windows 11 Pro', 'ESET', 'Operativo', 'Cargador Dell 65W, maletin', 'Equipo asignado a gerencia.', '2024-01-15', 'SI'),
    (2, 2, 'Equipo de escritorio', 'HP', 'ProDesk 400 G7', 'HP400G7-394X', 'AF-CSR-014', 'CSR-RECEPCION-01', 'Recepcion principal', '10.20.1.15', 'Intel Core i5-10500', '8 GB', 'DDR4', '1 TB', 'HDD', 'Windows 10 Pro', 'Windows Defender', 'En mantenimiento', 'Monitor HP 22, teclado, mouse', 'Presenta lentitud al iniciar.', '2023-08-20', 'SI'),
    (3, 3, 'Portatil', 'Lenovo', 'ThinkPad E14 Gen 4', 'LNE14-7Q2M9', 'AF-CNH-003', 'CNH-COORD-01', 'Coordinacion academica', '172.16.5.34', 'AMD Ryzen 5 5625U', '16 GB', 'DDR4', '512 GB', 'SSD', 'Windows 11 Pro', 'Kaspersky', 'Operativo', 'Cargador Lenovo USB-C', 'Bateria en buen estado.', '2024-02-05', 'SI'),
    (4, 4, 'Servidor', 'Dell', 'PowerEdge T150', 'DPT150-11F8S', 'AF-LDC-001', 'LDC-FILESERVER-01', 'Sala de comunicaciones', '10.30.0.10', 'Intel Xeon E-2314', '32 GB', 'DDR4 ECC', '2 TB RAID 1', 'HDD', 'Ubuntu Server 22.04 LTS', 'Otro', 'Operativo', 'UPS 1500 VA, monitor KVM', 'Servidor de archivos y copias de seguridad.', '2023-03-12', 'SI'),
    (5, 5, 'All in One', 'Apple', 'iMac 24 pulgadas M1', 'C02ZK0ABQ6L4', 'AF-GYA-009', 'GYA-DISENO-01', 'area de diseño', '192.168.50.28', 'Apple M1', '16 GB', 'Unificada', '512 GB', 'SSD', 'macOS Sonoma', 'Ninguno', 'Fuera de servicio', 'Teclado Magic Keyboard, Mouse Magic Mouse', 'No enciende; pendiente diagnostico de fuente.', '2022-11-30', 'NO');

INSERT INTO mantenimientos
    (id, equipo_id, tecnico_id, tipo_mantenimiento, fecha_programada, fecha_mantenimiento, fecha_finalizacion, estado, diagnostico, trabajo_realizado, repuestos_utilizados, limpieza_realizada, pasta_termica_aplicada, antivirus_actualizado, sistema_actualizado, respaldo_verificado, pruebas_funcionamiento, observaciones, costo)
VALUES
    (1, 1, 2, 'Preventivo', '2026-01-10', '2026-01-10 09:00:00', '2026-01-10 10:30:00', 'Completado', 'Equipo sin fallas; acumulacion leve de polvo en rejillas.', 'Limpieza externa e interna, actualizacion de Windows y revision de salud del disco.', 'No aplica', 1, 0, 1, 1, 1, 1, 'Se recomienda mantenimiento semestral.', 0.00),
    (2, 2, 3, 'Correctivo', '2026-02-03', '2026-02-03 14:00:00', '2026-02-03 16:45:00', 'Completado', 'Inicio lento por disco mecanico con sectores reasignados.', 'Se clono el sistema, se reemplazo el disco y se verifico el arranque.', 'SSD SATA 480 GB', 1, 0, 1, 1, 1, 1, 'Usuario valida acceso a aplicaciones de recepcion.', 285000.00),
    (3, 3, 2, 'Preventivo', '2026-03-18', '2026-03-18 08:30:00', '2026-03-18 09:40:00', 'Completado', 'Equipo operativo; actualizaciones pendientes.', 'Limpieza de ventilacion, instalacion de actualizaciones y analisis antivirus.', 'No aplica', 1, 0, 1, 1, 0, 1, 'No se requirieron repuestos.', 0.00),
    (4, 4, 4, 'Predictivo', '2026-04-22', '2026-04-22 19:00:00', '2026-04-22 20:30:00', 'Completado', 'Alertas de espacio disponible en volumen de respaldos.', 'Se depuraron respaldos vencidos, se reviso RAID y se documento capacidad.', 'No aplica', 0, 0, 0, 1, 1, 1, 'RAID saludable. Programar ampliacion de almacenamiento.', 0.00),
    (5, 5, 3, 'Diagnostico', '2026-05-06', '2026-05-06 11:00:00', NULL, 'En proceso', 'El equipo no enciende ni registra consumo estable con el adaptador.', 'Se realizaron pruebas de alimentacion y revision visual de la placa.', 'Pendiente definicion', 0, 0, 0, 0, 0, 0, 'Se cotizara diagnostico especializado para placa logica.', 0.00);

INSERT INTO evidencias (id, mantenimiento_id, nombre_archivo, ruta_archivo, tipo_archivo, descripcion) VALUES
    (1, 1, 'equipo_gerencia_despues.jpg', 'uploads/evidencias/equipo_gerencia_despues.jpg', 'image/jpeg', 'Estado del portatil despues de la limpieza.'),
    (2, 2, 'cambio_ssd_recepcion.jpg', 'uploads/evidencias/cambio_ssd_recepcion.jpg', 'image/jpeg', 'Instalacion del SSD en equipo de recepcion.'),
    (3, 3, 'informe_thinkpad.pdf', 'uploads/evidencias/informe_thinkpad.pdf', 'application/pdf', 'Informe de mantenimiento preventivo.'),
    (4, 4, 'revision_raid_servidor.jpg', 'uploads/evidencias/revision_raid_servidor.jpg', 'image/jpeg', 'Estado del arreglo RAID durante la revision.'),
    (5, 5, 'diagnostico_imac.jpg', 'uploads/evidencias/diagnostico_imac.jpg', 'image/jpeg', 'Registro visual de pruebas iniciales del iMac.');

INSERT INTO auditoria (usuario_id, accion, entidad, entidad_id, detalle, direccion_ip) VALUES
    (1, 'CREAR', 'cliente', 1, 'Cliente Soluciones Andinas S.A.S. registrado.', '127.0.0.1'),
    (2, 'CREAR', 'mantenimiento', 1, 'Mantenimiento preventivo completado para AND-GERENCIA-01.', '127.0.0.1'),
    (3, 'ACTUALIZAR', 'mantenimiento', 2, 'Mantenimiento correctivo cerrado tras cambio de disco.', '127.0.0.1'),
    (4, 'CREAR', 'mantenimiento', 4, 'Revision predictiva de servidor registrada.', '127.0.0.1'),
    (3, 'ACTUALIZAR', 'equipo', 5, 'Equipo GYA-DISENO-01 marcado como Fuera de servicio.', '127.0.0.1');

-- Verificacion rapida tras importar:
-- SELECT COUNT(*) AS usuarios FROM usuarios;
-- SELECT COUNT(*) AS clientes FROM clientes;
-- SELECT COUNT(*) AS equipos FROM equipos;
-- SELECT COUNT(*) AS mantenimientos FROM mantenimientos;
