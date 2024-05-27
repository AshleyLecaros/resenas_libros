-- iniciar el servicio de PostgreSQL
sudo service postgresql start

-- iniciar la consola interactiva de PostgreSQL
sudo -u postgres psql;

--Crear base de datos
CREATE DATABASE resena_libross

-- insertar datos a autores
INSERT INTO autores (autores_id, nombre) VALUES
(1, 'Gabriel García Márquez'),....

-- insertar datos a generos
INSERT INTO genero (genero_id, nombre) VALUES
(1, 'Ficción'), ....

-- insertar datos a libros
INSERT INTO libros (libros_id, titulo, descripcion, año_publicacion, portada_url, genero_id, autores_id) VALUES
(1, 'Cien años de soledad', 'Novela sobre la historia de la familia Buendía en Macondo.', 1967, 'https://url-de-la-portada.com', 1, 1), ....

-- insertar datos a usuarios
INSERT INTO usuarios (usuarios_id, nombre, email, tipo_usuario, is_active, is_staff, contraseña)
VALUES
(1, 'Juan Pérez', 'juan@example.com', 'Lector', TRUE, FALSE, 'CONTRASSEÑA'), ...

-- insertar datos a reseñas
INSERT INTO reseñas (reseña_id, libro_id, usuario_id, calificacion, comentario, fecha_reseña)
VALUES
(1, 1, 1, 5, 'Uno de los mejores libros que he leído.'),

