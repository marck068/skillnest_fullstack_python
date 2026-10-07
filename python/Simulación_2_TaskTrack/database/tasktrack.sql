CREATE DATABASE IF NOT EXISTS tasktrack
  CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE tasktrack;

CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    apellido VARCHAR(50) NOT NULL,
    email VARCHAR(120) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB;

CREATE TABLE categorias (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    usuario_id INT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE KEY uq_categoria_usuario (usuario_id, nombre),
    CONSTRAINT fk_categoria_usuario FOREIGN KEY (usuario_id)
        REFERENCES usuarios(id) ON DELETE CASCADE
) ENGINE=InnoDB;

CREATE TABLE tareas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(120) NOT NULL,
    categoria_id INT NOT NULL,
    prioridad ENUM('Alta','Media','Baja') NOT NULL DEFAULT 'Media',
    fecha_limite DATE NOT NULL,
    estado ENUM('Pendiente','En progreso','Completada') NOT NULL DEFAULT 'Pendiente',
    descripcion TEXT NOT NULL,
    usuario_id INT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX idx_tareas_usuario_fecha (usuario_id, fecha_limite),
    CONSTRAINT fk_tarea_categoria FOREIGN KEY (categoria_id)
        REFERENCES categorias(id) ON DELETE RESTRICT,
    CONSTRAINT fk_tarea_usuario FOREIGN KEY (usuario_id)
        REFERENCES usuarios(id) ON DELETE CASCADE
) ENGINE=InnoDB;

CREATE TABLE comentarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    tarea_id INT NOT NULL,
    usuario_id INT NOT NULL,
    texto VARCHAR(500) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_comentario_tarea FOREIGN KEY (tarea_id)
        REFERENCES tareas(id) ON DELETE CASCADE,
    CONSTRAINT fk_comentario_usuario FOREIGN KEY (usuario_id)
        REFERENCES usuarios(id) ON DELETE CASCADE
) ENGINE=InnoDB;

-- Datos de demostración. La contraseña para ambos usuarios es: Password123!
INSERT INTO usuarios (nombre, apellido, email, password) VALUES
('Marcelo', 'Rios', 'marcelo@tasktrack.cl', '$2a$10$N9qo8uLOickgx2ZMRZoMyeIjZAgcfl7p92ldGxad68LJZdL17lhWy'),
('Ana', 'Torres', 'ana@tasktrack.cl', '$2a$10$N9qo8uLOickgx2ZMRZoMyeIjZAgcfl7p92ldGxad68LJZdL17lhWy');

INSERT INTO categorias (nombre, usuario_id) VALUES
('Estudios', 1), ('Trabajo', 1), ('Salud', 1), ('Personal', 1),
('Estudios', 2), ('Trabajo', 2);

INSERT INTO tareas (titulo, categoria_id, prioridad, fecha_limite, estado, descripcion, usuario_id) VALUES
('Estudiar Flask', 1, 'Alta', DATE_ADD(CURDATE(), INTERVAL 3 DAY), 'Pendiente',
 'Repasar las rutas, modelos y controladores para el proyecto final de certificación.', 1),
('Proyecto final', 2, 'Media', DATE_ADD(CURDATE(), INTERVAL 8 DAY), 'En progreso',
 'Completar el CRUD de tareas, categorías y usuarios.', 1),
('Ir al gimnasio', 3, 'Baja', DATE_ADD(CURDATE(), INTERVAL 12 DAY), 'Completada',
 'Realizar la rutina semanal y registrar la actividad.', 1),
('Leer un libro', 4, 'Baja', DATE_ADD(CURDATE(), INTERVAL 15 DAY), 'Pendiente',
 'Leer el capítulo pendiente y anotar las ideas principales.', 1);

INSERT INTO comentarios (tarea_id, usuario_id, texto) VALUES
(1, 1, 'Repasar primero las rutas principales.'),
(2, 1, 'Ya está lista la estructura inicial.');
