--FUNCIONES
-- Que cliente uso mas su credito segun los actuales pedidos y como cambia su credito ? 

select p.idcliente,sum (dp.cantidad*dp.preciounitario) as monto_total_utilizado,cd.creditoinicial 
as credito_Inicial, cd.creditoActual - SUM(dp.cantidad * dp.precioUnitario) AS credito_ActualHoy 
from pedido p 
inner join detalle_pedido dp on dp.idpedido = p.idpedido 
inner join cliente c on c.idcliente = p.idcliente 
inner join credito cd on cd.idcredito = c.idcredito 
group by p.idcliente,cd.creditoinicial , cd.creditoactual  
ORDER BY monto_total_utilizado desc
limit 1;


CREATE FUNCTION CreditoActual2(IdclienteA smallint)
RETURNS TABLE (idCliente smallint, montoTotalUtilizado DECIMAL, creditoInicial DECIMAL, creditoActualHoy DECIMAL)
AS $$
BEGIN
    RETURN QUERY
    SELECT p.idCliente,
           SUM(dp.cantidad * dp.precioUnitario) AS monto_total_utilizado,
           cd.creditoInicial AS credito_Inicial,
           cd.creditoActual - SUM(dp.cantidad * dp.precioUnitario) AS credito_ActualHoy
    FROM pedido p
    INNER JOIN detalle_pedido dp ON dp.idPedido = p.idPedido
    INNER JOIN cliente c ON c.idCliente = p.idCliente
    INNER JOIN credito cd ON cd.idCredito = c.idCredito
    WHERE p.idCliente = IdclienteA
    GROUP BY p.idCliente, cd.creditoInicial, cd.creditoActual
    ORDER BY monto_total_utilizado DESC;
END;
$$ LANGUAGE plpgsql;


SELECT * FROM CreditoActual2(3::smallint);



-- FUNCION 2
-- determinar que empleado tiene clientes cuyas deudas son menores (es decir, que pagan más sus deudas)
-- según su deuda total, necesitas calcular la deuda total de cada cliente y luego compararla con la deuda 
--de otros clientes asociados a cada empleado

 


CREATE FUNCTION empleadoConClientesDeudasMenores()
RETURNS TABLE (nombre_empleado VARCHAR, id_cliente INT, deuda_cliente DECIMAL)
AS $$
BEGIN
    RETURN QUERY
    SELECT e.nombre AS nombre_empleado,
           c.idCliente AS id_cliente,
           SUM(dp.cantidad * dp.precioUnitario) AS deuda_cliente
    FROM empleado e
    INNER JOIN pedido p ON p.idempleado = e.idempleado
    INNER JOIN pago pg ON pg.idpedido = p.idpedido
    INNER JOIN detalle_pedido dp ON dp.idpedido = p.idpedido
    INNER JOIN cliente c ON c.idcliente = p.idcliente
    GROUP BY e.nombre, c.idCliente
    HAVING SUM(dp.cantidad * dp.precioUnitario) > 0
    ORDER BY e.nombre, deuda_cliente ASC;

END;
$$ LANGUAGE plpgsql;

SELECT * FROM empleadoConClientesDeudasMenores();
-- PROCEDIMIENTO CRUD 

-- CREAR
CREATE OR REPLACE PROCEDURE ClienteCrear(
    IN accion VARCHAR(10),
    IN nombres_cliente VARCHAR(50),
    IN apellido_paterno VARCHAR(50),
    IN apellido_materno VARCHAR(50),
    IN celular_cliente VARCHAR(20),
    IN id_credito_cliente SMALLINT
)
LANGUAGE plpgsql
AS $$
BEGIN
    IF accion = 'Agregar' THEN
        INSERT INTO cliente (nombres, apellidoPaterno, apellidoMaterno, celular, idCredito)
        VALUES (nombres_cliente, apellido_paterno, apellido_materno, celular_cliente, id_credito_cliente);
    
    ELSE
        RAISE EXCEPTION 'Acción no válida. Procedimiento destinando a agregar';
    END IF;
END;
$$;
call clientecrear('Agregar', 'Melissa Belen','Morales', 'Flores', '79961146', null ) 
call clientecrear('Agregar', 'Kesha','Mamani', 'Chinesse', '79978695', null ) 
-------------------
--LEER

CREATE OR REPLACE FUNCTION LeerClientesID(id_cliente INT)
RETURNS TABLE (
    idCliente INT,
    nombres VARCHAR(50),
    apellidoPaterno VARCHAR(50),
    apellidoMaterno VARCHAR(50),
    celular VARCHAR(20),
    idCredito SMALLINT,
    estado SMALLINT,
    fechaRegistro TIMESTAMP,
    fechaActualizacion TIMESTAMP
)
LANGUAGE plpgsql
AS $$
BEGIN
    RETURN QUERY SELECT * FROM cliente WHERE id_cliente = idCliente;
END;
$$;


call leerclientes (1)

select * from cliente where idcliente =1
-------------------------
-- MODIFICAR


CREATE OR REPLACE PROCEDURE ClienteModificar(
    in ID_CLIENTE int, 
    IN nombres_cliente VARCHAR(50),
    IN apellido_paterno VARCHAR(50),
    IN apellido_materno VARCHAR(50),
    IN celular_cliente VARCHAR(20),
    IN id_credito_cliente SMALLINT
)
LANGUAGE plpgsql
AS $$
BEGIN
        UPDATE cliente
        SET nombres = nombres_cliente,
            apellidoPaterno = apellido_paterno,
            apellidoMaterno = apellido_materno,
            celular = celular_cliente,
            idCredito = id_credito_cliente,
            fechaActualizacion = CURRENT_TIMESTAMP
        WHERE idCliente = id_cliente;
    
END;
$$;

call clienteModificar ( 12,'Keyla','Mamani','Chinesse', '799734379', null )

-------------
-- ELIMINAR

CREATE OR REPLACE PROCEDURE ClienteEliminar(
    in ID_CLIENTE int
   
)
LANGUAGE plpgsql
AS $$
BEGIN
        UPDATE cliente
        SET estado= 0
        WHERE idCliente = id_cliente;
    
END;
$$;

call clienteeliminar (12)

--------------
--- PEDIDOS 
-- CREAR
CREATE OR REPLACE PROCEDURE PedidoCrear(
    IN id_cliente int,
    IN id_empleado int,
    IN fecha_Entrega timestamp
  
)
LANGUAGE plpgsql
AS $$
BEGIN
        INSERT INTO pedido (idcliente, idempleado, fecha)
        VALUES (id_cliente, id_empleado,fecha_entrega );
    
    
END;
$$;
call pedidocrear (11,1,'2024-06-04 10:00:00')


-- VER
CREATE OR REPLACE PROCEDURE ObtenerPedidoPorID(
    IN id_pedido INT
)
LANGUAGE SQL
AS $$
    SELECT * FROM pedido WHERE idPedido = id_pedido;
$$;



--MODIFICAR
CREATE OR REPLACE PROCEDURE ModificarPedido(
    IN id_pedido INT,
    IN nuevo_id_cliente int,
    IN nuevo_id_empleado int,
    IN nueva_fecha TIMESTAMP)
LANGUAGE plpgsql
AS $$
BEGIN
    UPDATE pedido
    SET idCliente = nuevo_id_cliente,
        idEmpleado = nuevo_id_empleado,
        fecha = nueva_fecha,
        fechaActualizacion = CURRENT_TIMESTAMP
    WHERE idPedido = id_pedido;
END;
$$;
CALL ModificarPedido(14, 10, 1, '2024-04-06 12:30:00');


-- ELIMINAR  
CREATE OR REPLACE PROCEDURE PedidoEliminar(
    in ID_pedido int
   
)
LANGUAGE plpgsql
AS $$
BEGIN
        UPDATE pedido
        SET estado= 0
        WHERE idpedido = id_pedido;
    
END;
$$;

call pedidoeliminar (14)


 
    
 

