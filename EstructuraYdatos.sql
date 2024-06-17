CREATE TABLE cliente (
  idCliente SERIAL PRIMARY KEY,
  nombres varchar(50) NOT NULL,
  apellidoPaterno varchar(50) NOT NULL,
  apellidoMaterno varchar(50),
  celular varchar(20), 
  idCredito smallint , 
  estado smallint NOT NULL DEFAULT 1,
  fechaRegistro timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  fechaActualizacion timestamp,
  FOREIGN KEY (idCredito) REFERENCES credito (idCredito) ON DELETE CASCADE ON UPDATE CASCADE
);

INSERT INTO cliente VALUES 
  (1,'Juan','Perez','Sanchez','7985896759',1,1,'2019-11-16 17:54:18','2019-11-16 17:54:18'),
  (2,'Jose','Sanchez','Vargas','79858944859',2,1,'2019-11-16 17:54:18','2019-11-16 17:54:18'),
  (3,'Armando','Hoyos',NULL,'7985456859',3,1,'2019-11-16 17:54:18','2019-11-16 17:54:18'),
  (4,'Maria','Ramirez','Luna','7934896859',4,1,'2019-11-16 17:54:18','2019-11-16 17:54:18'),
  (5,'Viviana','Gutierrez','Miranda','7535896859',5,1,'2019-11-16 17:54:18','2019-11-16 17:54:18'),
  (6,'Julia','Vargas','Montes','798589659',6,1,'2019-11-16 17:54:18','2019-11-16 17:54:18'),
  (7,'Marcela ','Torrico','Siles','798575659',7,1,'2019-11-16 17:54:18','2019-11-16 17:54:18'),
  (8,'Magali Liliana','Merida','Suarez','7943896859',8,1,'2019-11-16 17:54:18','2019-11-16 17:54:18'),
  (9,'Guillermina','Peñarrieta','Flores','7958896859',9,1,'2019-11-16 17:54:18','2019-11-16 17:54:18'),
  (10,'David','Gutierrez','Mendez','7949386859',10,1,'2019-11-16 17:54:18','2019-11-16 17:54:18');
 
 -- Creditos
 -- 50000.00, 20000.00,,60000.00,44000.00,,30000.00,,15000.00,,11000.00,80000.00,5200.00,11999.00
 
 CREATE TABLE oficina (
  idOficina SERIAL PRIMARY KEY,
  nombreOficina varchar(40) NOT NULL,
  direccion varchar(100),
  estado smallint NOT NULL DEFAULT 1,
  fechaRegistro timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  fechaActualizacion timestamp
);

INSERT INTO oficina VALUES 
  (1,'Oficina Center','Cine Center, Planta baja, Nro 1A',1,'2019-11-16 17:54:46','2019-11-16 17:54:46'),
  (2,'Oficina IC Norte 1','IC Norte, Melchor Perez de Olguin, 2do Piso',1,'2019-11-16 17:54:46','2019-11-16 17:54:46'),
  (3,'Oficina IC Norte 2','IC Norte, Av. America, 2do Piso, Nro 2-12',1,'2019-11-16 17:54:46','2019-11-16 17:54:46'),
  (4,'Oficina Heroinas','Avenida Heroinas 745, Ayacucho y Junin',1,'2019-11-16 17:54:46','2019-11-16 17:54:46'),
  (5,'Oficina Prado','Avenida Ballivian 789 y Oruro',1,'2019-11-16 17:54:46','2019-11-16 17:54:46');
 
 CREATE TABLE empleado (
  idEmpleado SERIAL PRIMARY KEY,
  idOficina smallint NOT NULL,
  nombre varchar(50) NOT NULL,
  fechaNacimiento date NOT NULL,
  nombreUsuario varchar(50) NOT NULL,
  password varchar(50) NOT NULL,
  estado smallint NOT NULL DEFAULT 1,
  fechaRegistro timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  fechaActualizacion timestamp,
  FOREIGN KEY (idOficina) REFERENCES oficina (idOficina) ON DELETE CASCADE ON UPDATE CASCADE
);
INSERT INTO empleado VALUES 
  (1,1,'Jaime','1995-02-07','jaime','fde2fdb1dbf604aede0ffee76d26e4ce',1,'2019-11-16 17:56:25','2019-11-16 17:56:25'),
  (2,1,'Jose','1998-06-27','jose','662eaa47199461d01a623884080934ab',1,'2019-11-16 17:56:25','2019-11-16 17:56:25'),
  (3,2,'Gabriela','1996-09-25','gabriela','276e697e74e8b5264465139a480db556',1,'2019-11-16 17:56:25','2019-11-16 17:56:25'),
  (4,2,'Paulo','1990-05-28','paulo','dd41cb18c930753cbecf993f828603dc',1,'2019-11-16 17:56:25','2019-11-16 17:56:25'),
  (5,3,'Tony','1985-03-13','tony','ddc5f5e86d2f85e1b1ff763aff13ce0a',1,'2019-11-16 17:56:25','2019-11-16 17:56:25'),
  (6,4,'Junior','1989-06-13','junior','b03e3fd2b3d22ff6df2796c412b09311',1,'2019-11-16 17:56:25','2019-11-16 17:56:25'),
  (7,5,'Mirtha','1994-08-04','mirtha','9592e419fcf1e13324e5fee29d428bd3',1,'2019-11-16 17:56:25','2019-11-16 17:56:25'),
  (8,2,'Ivan','1994-12-12','ivan','2c42e5cf1cdbafea04ed267018ef1511',1,'2019-11-16 17:56:25','2019-11-16 17:56:25');

 CREATE TABLE credito (
  idCredito SERIAL PRIMARY KEY,
  creditoInicial decimal(8,2) not null,
  creditoActual decimal(8,2) not null,
  estado smallint NOT NULL DEFAULT 1,
  fechaRegistro timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  fechaActualizacion timestamp
);

INSERT into credito  VALUES 
  (1,50000.00,40000.00,1,'2019-11-16 17:54:18','2019-11-16 17:54:18'),
  (2, 20000.00, 18000.00,1,'2019-11-16 17:54:18','2019-11-16 17:54:18'),
  (3,60000.00,50000.00,1,'2019-11-16 17:54:18','2019-11-16 17:54:18'),
  (4,44000.00,42000.00,1,'2019-11-16 17:54:18','2019-11-16 17:54:18'),
  (5,30000.00,28000.00,1,'2019-11-16 17:54:18','2019-11-16 17:54:18'),
  (6,15000.00,15000.00,1,'2019-11-16 17:54:18','2019-11-16 17:54:18'),
  (7,11000.00,10000.00 ,1,'2019-11-16 17:54:18','2019-11-16 17:54:18'),
  (8,80000.00, 60000.00,1,'2019-11-16 17:54:18','2019-11-16 17:54:18'),
  (9, 5200.00,5000.00,1,'2019-11-16 17:54:18','2019-11-16 17:54:18'),
  (10,11999.00,11999.00,1,'2019-11-16 17:54:18','2019-11-16 17:54:18');
 
 CREATE TABLE producto (
  idProducto serial PRIMARY KEY,
  descripcion varchar(150) NOT NULL,
  unidadMedida varchar(25) NOT NULL,
  stock int NOT NULL,
  precioBase decimal(18,2) NOT NULL,
  estado smallint NOT NULL DEFAULT 1,
  fechaRegistro timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  fechaActualizacion timestamp NULL
);


INSERT INTO producto (descripcion, unidadMedida, stock, precioBase, estado, fechaRegistro, fechaActualizacion)
VALUES 
  ('Hojas Bond Oficio', 'Pieza', 150000, 0.10, 1, '2019-11-16 17:55:39', '2019-11-16 17:55:39'),
  ('Lapiz Negro HB 2.0', 'Pieza', 1000, 2.50, 1, '2019-11-16 17:55:39', '2019-11-16 17:55:39'),
  ('Borrador de Tinta', 'Pieza', 500, 5.00, 1, '2019-11-16 17:55:39', '2019-11-16 17:55:39'),
  ('Estuche Geométrico', 'Estuche', 250, 20.50, 1, '2019-11-16 17:55:39', '2019-11-16 17:55:39'),
  ('Cartulina de Color', 'Pliego', 400, 2.50, 1, '2019-11-16 17:55:39', '2019-11-16 17:55:39'),
  ('Archivador Rápido', 'Pieza', 4945, 3.00, 1, '2019-11-16 17:55:39', '2019-11-16 17:55:39'),
  ('Micropunta Negro 0.8', 'Pieza', 150, 8.50, 1, '2019-11-16 17:55:39', '2019-11-16 17:55:39'),
  ('Marcadores (12 Colores)', 'Estuche', 650, 35.00, 1, '2019-11-16 17:55:39', '2019-11-16 17:55:39'),
  ('Cuaderno 100 Hojas C/espiral', 'Pieza', 905, 21.00, 1, '2019-11-16 17:55:39', '2019-11-16 17:55:39'),
  ('Boligrafo Pilot Negro', 'Pieza', 1500, 5.00, 1, '2019-11-16 17:55:39', '2019-11-16 17:55:39'),
  ('Boligrafo Pilot Rojo', 'Pieza', 745, 5.00, 1, '2019-11-16 17:55:39', '2019-11-16 17:55:39'),
  ('Boligrafo Pilot Azul', 'Pieza', 800, 5.00, 1, '2019-11-16 17:55:39', '2019-11-16 17:55:39'),
  ('Pegamento de 250 ml', 'Bote', 234, 7.50, 1, '2019-11-16 17:55:39', '2019-11-16 17:55:39'),
  ('Acuarelas de color', 'Docena', 65, 24.50, 1, '2019-11-16 17:55:39', '2019-11-16 17:55:39');

 -- fin producto
 
 CREATE TABLE pedido (
  idPedido SERIAL PRIMARY KEY,
  idCliente smallint NOT NULL,
  idEmpleado smallint NOT NULL,
  fecha timestamp NOT NULL,
  estado smallint NOT NULL DEFAULT 1,
  fechaRegistro timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  fechaActualizacion timestamp,
  FOREIGN KEY (idCliente) REFERENCES cliente (idCliente) ON DELETE CASCADE ON UPDATE CASCADE,
  
  FOREIGN KEY (idEmpleado) REFERENCES empleado (idEmpleado) ON DELETE CASCADE ON UPDATE CASCADE
);

INSERT INTO pedido VALUES 
  (1, 1, 6, '2012-03-01 00:00:00', 1, '2019-11-16 17:55:06', '2019-11-16 17:55:06'),
  (2, 2, 4, '2012-03-02 00:00:00', 1, '2019-11-16 17:55:06', '2019-11-16 17:55:06'),
  (3, 3, 5, '2013-03-02 00:00:00', 1, '2019-11-16 17:55:06', '2019-11-16 17:55:06'),
  (4, 4, 7, '2012-03-01 00:00:00', 1, '2019-11-16 17:55:06', '2019-11-16 17:55:06'),
  (5, 5, 8, '2012-03-03 00:00:00', 1, '2019-11-16 17:55:06', '2019-11-16 17:55:06'),
  (6, 6, 1, '2012-03-05 00:00:00', 1, '2019-11-16 17:55:06', '2019-11-16 17:55:06'),-- este edite
  (7, 7, 6, '2012-03-03 00:00:00', 1, '2019-11-16 17:55:06', '2019-11-16 17:55:06'),
  (8, 8, 8, '2012-03-03 00:00:00', 1, '2019-11-16 17:55:06', '2019-11-16 17:55:06'),
  (9, 9, 1, '2012-03-03 00:00:00', 1, '2019-11-16 17:55:06', '2019-11-16 17:55:06'), -- este este
  (10, 1, 6, '2012-03-06 00:00:00', 1, '2019-11-16 17:55:06', '2019-11-16 17:55:06'), 
  (11, 9, 4, '2015-11-24 11:39:04', 1, '2019-11-16 17:55:06', '2019-11-16 17:55:06');
 
--Ojo por aca 
 
  CREATE TABLE detalle_pedido (
  idPedido int NOT NULL,
  idProducto int NOT NULL,
  cantidad int NOT NULL,
  precioUnitario decimal(8,2) NOT NULL,
  fechaEntrega timestamp not null,
  estado smallint NOT NULL DEFAULT 1,
  PRIMARY KEY (idPedido, idProducto),
  FOREIGN KEY (idPedido) REFERENCES pedido (idPedido) ON DELETE CASCADE ON UPDATE CASCADE,
  FOREIGN KEY (idProducto) REFERENCES producto (idProducto) ON DELETE CASCADE ON UPDATE CASCADE
);

INSERT INTO detalle_pedido VALUES 
  (1, 3, 25, 5.00, '2019-02-15', 1),
  (1, 5, 20, 2.50, '2019-05-10', 1),
  (1, 7, 10, 8.50, '2019-03-25', 1),
  (1, 9, 5, 21.00, '2019-09-12', 1),
  (1, 11, 80, 5.00, '2019-08-05', 1),
  (1, 14, 50, 24.50, '2019-10-30', 1),
  (2, 2, 50, 2.50, '2019-01-20', 1),
  (2, 4, 10, 20.50, '2019-04-03', 1),
  (2, 6, 15, 3.00, '2019-06-18', 1),
  (2, 8, 25, 35.00, '2019-07-29', 1),
  (2, 10, 20, 5.00, '2019-11-15', 1),
  (2, 12, 5, 5.00, '2019-12-05', 1),
  (2, 14, 10, 24.50, '2019-01-10', 1),
  (3, 4, 25, 20.50, '2019-05-25', 1),
  (3, 5, 30, 2.50, '2019-08-14', 1),
  (3, 6, 35, 3.00, '2019-10-20', 1),
  (3, 7, 15, 8.50, '2019-03-17', 1),
  (3, 8, 10, 35.00, '2019-04-29', 1),
  (3, 14, 5, 24.50, '2019-11-02', 1),
  (4, 6, 5, 3.00, '2019-12-01', 1),
  (4, 9, 5, 21.00, '2019-06-30', 1),
  (4, 10, 70, 5.00, '2019-02-14', 1),
  (4, 11, 10, 5.00, '2019-08-18', 1),
  (4, 12, 45, 5.00, '2019-04-07', 1),
  (4, 13, 35, 7.50, '2019-01-02', 1),
  (4, 14, 50, 24.50, '2019-10-15', 1),
  (5, 1, 2000, 0.10, '2019-05-03', 1),
  (5, 3, 35, 5.00, '2019-09-25', 1),
  (5, 6, 5, 3.00, '2019-07-12', 1),
  (5, 9, 10, 21.00, '2019-11-08', 1),
  (5, 13, 15, 7.50, '2019-02-28', 1),
  (5, 14, 20, 24.50, '2019-06-22', 1),
  (6, 1, 1000, 0.10, '2019-10-05', 1),
  (6, 2, 20, 2.50, '2019-08-03', 1),
  (6, 3, 10, 5.00, '2019-04-29', 1),
  (6, 4, 20, 20.50, '2019-06-21', 1),
  (6, 5, 10, 2.50, '2019-12-14', 1),
  (6, 6, 5, 3.00, '2019-01-18', 1),
  (6, 7, 10, 8.50, '2019-09-10', 1),
  (6, 8, 20, 35.00, '2019-03-07', 1),
  (7, 1, 1500, 0.10, '2019-07-20', 1),
  (7, 11, 5, 5.00, '2019-05-14', 1),
  (7, 12, 10, 5.00, '2019-11-29', 1),
  (7, 13, 25, 7.50, '2019-02-12', 1),
  (7, 14, 10, 24.50, '2019-06-04', 1),
  (8, 5, 5, 2.50, '2019-10-17', 1),
  (8, 6, 10, 3.00, '2019-08-01', 1),
  (8, 7, 5, 8.50, '2019-12-25', 1),
  (8, 8, 10, 35.00, '2019-02-22', 1),
  (8, 9, 15, 21.00, '2019-06-08', 1),
  (8, 10, 20, 5.00, '2019-03-13', 1),
  (8, 14, 30, 24.50, '2019-09-09', 1),
  (9, 10, 70, 5.00, '2019-05-02', 1),
  (9, 11, 15, 5.00, '2019-01-05', 1),
  (9, 12, 25, 5.00, '2019-03-27', 1),
  (9, 13, 50, 7.50, '2019-08-14', 1),
  (9, 14, 60, 24.50, '2019-11-18', 1),
  (10, 1, 200, 0.10, '2019-06-20', 1),
  (10, 2, 5, 2.50, '2019-12-30', 1),
  (10, 7, 5, 8.50, '2019-03-21', 1),
  (10, 8, 15, 35.00, '2019-11-11', 1),
  (10, 9, 10, 21.00, '2019-09-07', 1),
  (10, 12, 25, 5.00, '2019-05-16', 1),
  (10, 14, 30, 24.50, '2019-08-29', 1),
  (11, 6, 55, 3.00, '2019-04-10', 1);
 
 CREATE TABLE Pago (
    idPago SERIAL PRIMARY KEY,
    idPedido smallint,
    montoPagado INT,
    deudaActual INT,
    estado SMALLINT NOT NULL DEFAULT 1,
    fechaRegistro TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    fechaActualizacion TIMESTAMP NULL,
    FOREIGN KEY (idPedido) REFERENCES pedido (idPedido) ON DELETE CASCADE ON UPDATE CASCADE
);

-- sayuri yamile
INSERT INTO Pago (idPedido, montoPagado, deudaActual)
SELECT idPedido, (50-(cantidad * precioUnitario)), (cantidad * precioUnitario) AS deuda
FROM detalle_pedido;

select * from Pago

