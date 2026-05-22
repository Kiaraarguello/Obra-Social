-- ==========================================
-- ESTRUCTURA INICIAL DE BASE DE DATOS
-- ==========================================

-- Crear base de datos si no existe
CREATE DATABASE IF NOT EXISTS obra_social
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;

USE obra_social;

-- Tabla de afiliados (ejemplo práctico para el negocio de Obra Social)
CREATE TABLE IF NOT EXISTS afiliados (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    apellido VARCHAR(100) NOT NULL,
    dni VARCHAR(20) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE NULL,
    activo BOOLEAN DEFAULT TRUE,
    fecha_alta TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    INDEX (dni)
) ENGINE=InnoDB;

-- Insertar datos de prueba iniciales
INSERT INTO afiliados (nombre, apellido, DNI, email, activo) VALUES 
('Juan', 'Pérez', '35123456', 'juan.perez@email.com', 1),
('María', 'Gómez', '38987654', 'maria.gomez@email.com', 1),
('Carlos', 'Rodríguez', '41223344', 'carlos.rod@email.com', 0)
ON DUPLICATE KEY UPDATE dni=dni;
