
-- FUNCION 1
select p.idcliente,sum (dp.cantidad*dp.preciounitario) as monto_total_utilizado,cd.creditoinicial 
as credito_Inicial, cd.creditoActual - SUM(dp.cantidad * dp.precioUnitario) AS credito_ActualHoy 
from pedido p 
inner join detalle_pedido dp on dp.idpedido = p.idpedido 
inner join cliente c on c.idcliente = p.idcliente 
inner join credito cd on cd.idcredito = c.idcredito 
group by p.idcliente,cd.creditoinicial , cd.creditoactual  
ORDER BY monto_total_utilizado desc
limit 1;


select * from CreditoActual2(9::smallint);

-- FUNCION 2

CREATE OR REPLACE FUNCTION top_5_clientes_mas_pagos2()
RETURNS TABLE (
    ClienteID INT,
    Nombre VARCHAR(50),
    ApellidoPaterno VARCHAR(50),
    TotalDeuda DECIMAL(10, 2),
    TotalPagos DECIMAL(10, 2)
) AS $$
BEGIN
    RETURN QUERY
    SELECT
        c.idCliente AS ClienteID,
        c.nombres AS Nombre,
        c.apellidoPaterno AS ApellidoPaterno,
        COALESCE(SUM(dp.cantidad * dp.precioUnitario)::NUMERIC, 0) AS TotalDeuda,
        COALESCE(SUM(pg.montoPagado)::NUMERIC, 0) AS TotalPagos
    FROM
        cliente c
    LEFT JOIN
        pedido pd ON c.idCliente = pd.idCliente
    LEFT JOIN
        detalle_pedido dp ON pd.idPedido = dp.idPedido
    LEFT JOIN
        pago pg ON pd.idPedido = pg.idPedido
    GROUP BY
        c.idCliente, c.nombres, c.apellidoPaterno
    ORDER BY
        TotalPagos DESC
    LIMIT 5;
END;
$$ LANGUAGE plpgsql;


select * from top_5_clientes_mas_pagos2() 

-- FUNCION 3

CREATE OR REPLACE FUNCTION obtener_producto_mas_pedidos2()
RETURNS TABLE(id_producto INT, producto VARCHAR, total_pedidos BIGINT) AS $$
BEGIN
    RETURN QUERY
    SELECT
        p.idProducto,
        p.descripcion AS Producto,
        COUNT(dp.idPedido) AS TotalPedidos
    FROM
        producto p
    LEFT JOIN
        detalle_pedido dp ON p.idProducto = dp.idProducto
    GROUP BY
        p.idProducto, p.descripcion
    ORDER BY
        TotalPedidos DESC
    LIMIT 1;
END;
$$ LANGUAGE plpgsql;


select * from obtener_producto_mas_pedidos2()


-- Vistas

CREATE OR REPLACE VIEW vista_pedidos_producto1 AS
SELECT
    p.idProducto,
    p.descripcion AS Producto,
    COUNT(dp.idPedido) AS TotalPedidos
FROM
    producto p
LEFT JOIN
    detalle_pedido dp ON p.idProducto = dp.idProducto
GROUP BY
    p.idProducto, p.descripcion
ORDER BY
    TotalPedidos DESC; 

SELECT * FROM vista_pedidos_producto1;

-- Vista 2
CREATE OR REPLACE VIEW vista_cliente_deuda_credito AS
SELECT
    c.idCliente,
    CONCAT(c.nombres, ' ', c.apellidoPaterno) AS NombreCliente,
    COUNT(p.idPedido) AS TotalPedidos,
    COALESCE(SUM(dp.cantidad * dp.precioUnitario), 0) AS TotalDeuda,
    cr.creditoInicial AS CreditoInicial
FROM
    cliente c
LEFT JOIN
    pedido p ON c.idCliente = p.idCliente
LEFT JOIN
    detalle_pedido dp ON p.idPedido = dp.idPedido
LEFT JOIN
    credito cr ON c.idCredito = cr.idCredito
GROUP BY
    c.idCliente, NombreCliente, cr.creditoInicial
ORDER BY
    totalpedidos DESC; 


select * from vista_cliente_deuda_credito;
