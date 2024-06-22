from sqlalchemy import Column, Integer, String, Date, ForeignKey, TIMESTAMP, SmallInteger, DECIMAL,func

from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class Credito(Base):
    __tablename__ = 'credito'
    idcredito = Column(Integer, primary_key=True)
    creditoinicial = Column(DECIMAL(8,2), nullable=False)
    creditoactual = Column(DECIMAL(8,2), nullable=True)
    estado = Column(SmallInteger, nullable=False, default=1)
    fecharegistro = Column(TIMESTAMP, nullable=False, server_default='CURRENT_TIMESTAMP')
    fechaactualizacion = Column(TIMESTAMP)
    
    @staticmethod
    def mostrar_todos_los_creditos(session):
        creditos = session.query(Credito).filter(Credito.estado==1).all()
        for credito in creditos:
            print("ID de Crédito:", credito.idcredito)
            print("Crédito Inicial:", credito.creditoinicial)
            print("Crédito Actual:", credito.creditoactual)
            print("Estado:", credito.estado)
            print("Fecha de Registro:", credito.fecharegistro)
            print("Fecha de Actualización:", credito.fechaactualizacion)
            print("-------------------------------------------")

    @staticmethod
    def mostrar_credito_por_id(session, id_credito):
        credito = session.query(Credito).filter(Credito.idcredito == id_credito, Credito.estado==1).first()
        if credito:
            print('CRÉDITO ENCONTRADO')
            print("ID de Crédito:", credito.idcredito)
            print("Crédito Inicial:", credito.creditoinicial)
            print("Crédito Actual:", credito.creditoactual)
            print("Estado:", credito.estado)
            print("Fecha de Registro:", credito.fecharegistro)
            print("Fecha de Actualización:", credito.fechaactualizacion)
            print("-------------------------------------------")
        else:
            print('No existe el crédito mencionado')

    @staticmethod
    def agregar_credito(session, creditoinicial, creditoactual, estado=1):
        nuevo_credito = Credito(creditoinicial=creditoinicial, creditoactual=creditoactual, estado=estado)
        session.add(nuevo_credito)
        session.commit()
        print('Se ha agregado un nuevo crédito')

    @staticmethod
    def modificar_credito(session, id_credito, **kwargs):
        credito = session.query(Credito).filter_by(idcredito=id_credito).first()
        if credito:
            for key, value in kwargs.items():
                setattr(credito, key, value)
            session.commit()
            print('Crédito actualizado')
        else:
            print('Crédito no encontrado')

    
  

class Cliente(Base):
    __tablename__ = 'cliente'
    idcliente = Column(Integer, primary_key=True)
    nombres  = Column(String(45), nullable=False)
    apellidopaterno = Column(String(45), nullable=False)
    apellidomaterno = Column(String(45), nullable=True)
    celular = Column(String(45), nullable=True)
    idcredito = Column(Integer, ForeignKey('credito.idcredito'), nullable=True)
    estado = Column(Integer, default=1)
    fecharegistro = Column(TIMESTAMP, nullable=False, server_default=func.current_TIMESTAMP()) 
    fechaactualizacion = Column(TIMESTAMP)
    @staticmethod
    def mostrar_todos_los_clientes(session):
        clientes = session.query(Cliente).filter(Cliente.estado == 1).all()
        for cliente in clientes:
            print("ID de Cliente:", cliente.idcliente)
            print("Nombres:", cliente.nombres)
            print("Apellido Paterno:", cliente.apellidopaterno)
            print("Apellido Materno:", cliente.apellidomaterno)
            print("Celular:", cliente.celular)
            print("ID de Crédito:", cliente.idcredito)
            print("Estado:", cliente.estado)
            print("Fecha de Registro:", cliente.fecharegistro)
            print("Fecha de Actualización:", cliente.fechaactualizacion)
            print("-------------------------------------------")

    @staticmethod
    def mostrar_cliente_por_id(session, id_cliente):
        cliente = session.query(Cliente).filter(Cliente.idcliente == id_cliente, Cliente.estado==1).first()
        if cliente:
            print('CLIENTE ENCONTRADO')
            print("ID de Cliente:", cliente.idcliente)
            print("Nombres:", cliente.nombres)
            print("Apellido Paterno:", cliente.apellidopaterno)
            print("Apellido Materno:", cliente.apellidomaterno)
            print("Celular:", cliente.celular)
            print("ID de Crédito:", cliente.idcredito)
            print("Estado:", cliente.estado)
            print("Fecha de Registro:", cliente.fecharegistro)
            print("Fecha de Actualización:", cliente.fechaactualizacion)
            print("-------------------------------------------")
        else:
            print('No existe el cliente mencionado')

    @staticmethod
    def agregar_cliente(session, nombres, apellido_paterno, apellido_materno=None, celular1=None, id_credito=None):
        nuevo_cliente = Cliente(nombres=nombres, apellidopaterno=apellido_paterno, apellidomaterno=apellido_materno, celular=celular1, idcredito=id_credito,estado=1 )
        session.add(nuevo_cliente)
        session.commit()
        print('Se ha agregado un nuevo cliente')

    @staticmethod
    def modificar_cliente(session, id_cliente, **kwargs):
        cliente = session.query(Cliente).filter_by(idcliente=id_cliente).first()
        if cliente:
            for key, value in kwargs.items():
                setattr(cliente, key, value)
            session.commit()
            print('Cliente actualizado')
        else:
            print('Cliente no encontrado')

    @staticmethod
    def eliminar_cliente(session, id_cliente):
        cliente = session.query(Cliente).filter_by(idcliente=id_cliente).first()
        if cliente:
            session.delete(cliente)
            session.commit()
            print('Cliente eliminado')
        else:
            print('Cliente no encontrado')


class Oficina(Base):
    __tablename__ = 'oficina'
    idoficina = Column(Integer, primary_key=True)
    nombreoficina = Column(String(40), nullable=False)
    direccion = Column(String(100))
    estado = Column(Integer, default=1)
    fecharegistro = Column(TIMESTAMP, nullable=False, server_default=func.current_TIMESTAMP()) 
    fechaactualizacion = Column(TIMESTAMP)
    
    @staticmethod
    def mostrar_todas_las_oficinas(session):
        oficinas = session.query(Oficina).all()
        for oficina in oficinas:
            print("ID de Oficina:", oficina.idoficina)
            print("Nombre de Oficina:", oficina.nombreoficina)
            print("Dirección:", oficina.direccion)
            print("Estado:", oficina.estado)
            print("Fecha de Registro:", oficina.fecharegistro)
            print("Fecha de Actualización:", oficina.fechaactualizacion)
            print("-------------------------------------------")

    @staticmethod
    def mostrar_oficina_por_id(session, id_oficina):
        oficina = session.query(Oficina).filter(Oficina.idoficina == id_oficina).first()
        if oficina:
            print('OFICINA ENCONTRADA')
            print("ID de Oficina:", oficina.idoficina)
            print("Nombre de Oficina:", oficina.nombreoficina)
            print("Dirección:", oficina.direccion)
            print("Estado:", oficina.estado)
            print("Fecha de Registro:", oficina.fecharegistro)
            print("Fecha de Actualización:", oficina.fechaactualizacion)
            print("-------------------------------------------")
        else:
            print('No existe la oficina mencionada')

    @staticmethod
    def agregar_oficina(session, nombre_oficina, direccion=None, estado=1):
        nueva_oficina = Oficina(nombreoficina=nombre_oficina, direccion=direccion, estado=estado)
        session.add(nueva_oficina)
        session.commit()
        print('Se ha agregado una nueva oficina')

    @staticmethod
    def modificar_oficina(session, id_oficina, **kwargs):
        oficina = session.query(Oficina).filter_by(idoficina=id_oficina).first()
        if oficina:
            for key, value in kwargs.items():
                setattr(oficina, key, value)
            session.commit()
            print('Oficina actualizada')
        else:
            print('Oficina no encontrada')

    @staticmethod
    def eliminar_oficina(session, id_oficina):
        oficina = session.query(Oficina).filter_by(idoficina=id_oficina).first()
        if oficina:
            session.delete(oficina)
            session.commit()
            print('Oficina eliminada')
        else:
            print('Oficina no encontrada')


class Empleado(Base):
    __tablename__ = 'empleado'
    idempleado = Column(Integer, primary_key=True)
    idoficina = Column(Integer, ForeignKey('oficina.idoficina'), nullable=False)
    nombre = Column(String(50), nullable=False)
    fechanacimiento = Column(Date, nullable=False)
    nombreusuario = Column(String(50), nullable=False)
    password = Column(String(50), nullable=False)
    estado = Column(Integer, default=1)
    fecharegistro = Column(TIMESTAMP, nullable=False, server_default=func.current_TIMESTAMP()) 
    fechaactualizacion = Column(TIMESTAMP)
    
    @staticmethod
    def mostrar_todos_los_empleados(session):
        empleados = session.query(Empleado).filter(Empleado.estado == 1).all()
        
        for empleado in empleados:
            print("ID de Empleado:", empleado.idempleado)
            print("ID de Oficina:", empleado.idoficina)
            print("Nombre:", empleado.nombre)
            print("Fecha de Nacimiento:", empleado.fechanacimiento)
            print("Nombre de Usuario:", empleado.nombreusuario)
            print("Contraseña:", empleado.password)
            print("Estado:", empleado.estado)
            print("Fecha de Registro:", empleado.fecharegistro)
            print("Fecha de Actualización:", empleado.fechaactualizacion)
            print("-------------------------------------------")

    @staticmethod
    def mostrar_empleado_por_id(session, id_empleado):
        empleado = session.query(Empleado).filter(Empleado.idempleado == id_empleado, Empleado.estado==1).first()
        if empleado:
            print('EMPLEADO ENCONTRADO')
            print("ID de Empleado:", empleado.idempleado)
            print("ID de Oficina:", empleado.idoficina)
            print("Nombre:", empleado.nombre)
            print("Fecha de Nacimiento:", empleado.fechanacimiento)
            print("Nombre de Usuario:", empleado.nombreusuario)
            print("Contraseña:", empleado.password)
            print("Estado:", empleado.estado)
            print("Fecha de Registro:", empleado.fecharegistro)
            print("Fecha de Actualización:", empleado.fechaactualizacion)
            print("-------------------------------------------")
        else:
            print('No existe el empleado mencionado')

    @staticmethod
    def agregar_empleado(session, id_oficina, nombre, fecha_nacimiento, nombre_usuario, password, estado=1):
        nuevo_empleado = Empleado(idoficina=id_oficina, nombre=nombre, fechanacimiento=fecha_nacimiento,
                                  nombreusuario=nombre_usuario, password=password, estado=1)
        session.add(nuevo_empleado)
        session.commit()
        print('Se ha agregado un nuevo empleado')

    @staticmethod
    def modificar_empleado(session, id_empleado, **kwargs):
        empleado = session.query(Empleado).filter_by(idempleado=id_empleado).first()
        if empleado:
            for key, value in kwargs.items():
                setattr(empleado, key, value)
            session.commit()
            print('Empleado actualizado')
        else:
            print('Empleado no encontrado')

    @staticmethod
    def eliminar_empleado(session, id_empleado):
        empleado = session.query(Empleado).filter_by(idempleado=id_empleado).first()
        if empleado:
            session.delete(empleado)
            session.commit()
            print('Empleado eliminado')
        else:
            print('Empleado no encontrado')





class Producto(Base):
    __tablename__ = 'producto'
    idproducto = Column(Integer, primary_key=True)
    descripcion = Column(String(150), nullable=False)
    unidadmedida = Column(String(25), nullable=False)
    stock = Column(Integer, nullable=False)
    preciobase = Column(DECIMAL(18, 2), nullable=False)
    estado = Column(Integer, default=1)
    fecharegistro = Column(TIMESTAMP, nullable=False, server_default=func.current_TIMESTAMP()) 
    fechaactualizacion = Column(TIMESTAMP)
    

    @staticmethod
    def mostrar_todos_los_productos(session):
        productos = session.query(Producto).filter(Producto.estado==1).all()
        for producto in productos:
            print("ID de Producto:", producto.idproducto)
            print("Descripción:", producto.descripcion)
            print("Unidad de Medida:", producto.unidadmedida)
            print("Stock:", producto.stock)
            print("Precio Base:", producto.preciobase)
            print("Estado:", producto.estado)
            print("Fecha de Registro:", producto.fecharegistro)
            print("Fecha de Actualización:", producto.fechaactualizacion)
            print("-------------------------------------------")

    @staticmethod
    def mostrar_producto_por_id(session, id_producto):
        producto = session.query(Producto).filter(Producto.idProducto == id_producto, Producto.estado==1).first()
        if producto:
            print('PRODUCTO ENCONTRADO')
            print("ID de Producto:", producto.idproducto)
            print("Descripción:", producto.descripcion)
            print("Unidad de Medida:", producto.unidadmedida)
            print("Stock:", producto.stock)
            print("Precio Base:", producto.preciobase)
            print("Estado:", producto.estado)
            print("Fecha de Registro:", producto.fecharegistro)
            print("Fecha de Actualización:", producto.fechaactualizacion)
            print("-------------------------------------------")
        else:
            print('No existe el producto mencionado')

    @staticmethod
    def agregar_producto(session, descripcion, unidad_medida, stock, precio_base, estado=1):
        nuevo_producto = Producto(descripcion=descripcion, unidadmedida=unidad_medida, stock=stock,
                                  preciobase=precio_base, estado=1)
        session.add(nuevo_producto)
        session.commit()
        print('Se ha agregado un nuevo producto')

    @staticmethod
    def modificar_producto(session, id_producto, **kwargs):
        producto = session.query(Producto).filter_by(idProducto=id_producto).first()
        if producto:
            for key, value in kwargs.items():
                setattr(producto, key, value)
            session.commit()
            print('Producto actualizado')
        else:
            print('Producto no encontrado')

    @staticmethod
    def eliminar_producto(session, id_producto):
        producto = session.query(Producto).filter_by(idproducto=id_producto).first()
        if producto:
            session.delete(producto)
            session.commit()
            print('Producto eliminado')
        else:
            print('Producto no encontrado')


class Pedido(Base):
    __tablename__ = 'pedido'
    idpedido = Column(Integer, primary_key=True)
    idcliente = Column(Integer, ForeignKey('cliente.idcliente'), nullable=False)
    idempleado = Column(Integer, ForeignKey('empleado.idempleado'), nullable=False)
    fecha = Column(TIMESTAMP, nullable=False)
    estado = Column(Integer, default=1)
    fecharegistro = Column(TIMESTAMP, nullable=False, server_default=func.current_TIMESTAMP()) 
    fechaactualizacion = Column(TIMESTAMP)
    

    


    @staticmethod
    def mostrar_todos_los_pedidos(session):
        pedidos = session.query(Pedido).all()
        for pedido in pedidos:
            print("ID de Pedido:", pedido.idpedido)
            print("ID de Cliente:", pedido.idcliente)
            print("ID de Empleado:", pedido.idempleado)
            print("Fecha:", pedido.fecha)
            print("Estado:", pedido.estado)
            print("Fecha de Registro:", pedido.fecharegistro)
            print("Fecha de Actualización:", pedido.fechaactualizacion)
            print("-------------------------------------------")

    @staticmethod
    def mostrar_pedido_por_id(session, id_pedido):
        pedido = session.query(Pedido).filter(Pedido.idpedido == id_pedido).first()
        if pedido:
            print('PEDIDO ENCONTRADO')
            print("ID de Pedido:", pedido.idpedido)
            print("ID de Cliente:", pedido.idcliente)
            print("ID de Empleado:", pedido.idempleado)
            print("Fecha:", pedido.fecha)
            print("Estado:", pedido.estado)
            print("Fecha de Registro:", pedido.fecharegistro)
            print("Fecha de Actualización:", pedido.fechaactualizacion)
            print("-------------------------------------------")
        else:
            print('No existe el pedido mencionado')

    @staticmethod
    def agregar_pedido(session, id_cliente, id_empleado, fecha, estado=1):
        nuevo_pedido = Pedido(idcliente=id_cliente, idempleado=id_empleado, fecha=fecha, estado=estado)
        session.add(nuevo_pedido)
        session.commit()
        print('Se ha agregado un nuevo pedido')

    @staticmethod
    def modificar_pedido(session, id_pedido, **kwargs):
        pedido = session.query(Pedido).filter_by(idpedido=id_pedido).first()
        if pedido:
            for key, value in kwargs.items():
                setattr(pedido, key, value)
            session.commit()
            print('Pedido actualizado')
        else:
            print('Pedido no encontrado')

    @staticmethod
    def eliminar_pedido(session, id_pedido):
        pedido = session.query(Pedido).filter_by(idpedido=id_pedido).first()
        if pedido:
            session.delete(pedido)
            session.commit()
            print('Pedido eliminado')
        else:
            print('Pedido no encontrado')



class DetallePedido(Base):
    __tablename__ = 'detalle_pedido'
    idpedido = Column(Integer, ForeignKey('pedido.idpedido'), primary_key=True)
    idproducto = Column(Integer, ForeignKey('producto.idproducto'), primary_key=True)
    cantidad = Column(Integer, nullable=False)
    preciounitario = Column(DECIMAL(8, 2), nullable=False)
    fechaentrega = Column(TIMESTAMP, nullable=False)
    estado = Column(Integer, nullable=False, default=1)

   
    @staticmethod
    def mostrar_todos_detalles_pedido(session):
        detalles_pedido = session.query(DetallePedido).all()
        for detalle in detalles_pedido:
            print("ID de Pedido:", detalle.idpedido)
            print("ID de Producto:", detalle.idproducto)
            print("Cantidad:", detalle.cantidad)
            print("Precio Unitario:", detalle.preciounitario)
            print("Fecha de Entrega:", detalle.fechaentrega)
            print("Estado:", detalle.estado)
            print("-------------------------------------------")

    @staticmethod
    def mostrar_detalle_pedido_por_id(session, id_pedido, id_producto):
        detalle = session.query(DetallePedido).filter_by(idPedido=id_pedido, idProducto=id_producto).first()
        if detalle:
            print('DETALLE DE PEDIDO ENCONTRADO')
            print("ID de Pedido:", detalle.idpedido)
            print("ID de Producto:", detalle.idproducto)
            print("Cantidad:", detalle.cantidad)
            print("Precio Unitario:", detalle.preciounitario)
            print("Fecha de Entrega:", detalle.fechaentrega)
            print("Estado:", detalle.estado)
            print("-------------------------------------------")
        else:
            print('No existe el detalle de pedido mencionado')

    @staticmethod
    def agregar_detalle_pedido(session, id_pedido, id_producto, cantidad, precio_unitario, fecha_entrega, estado=1):
        nuevo_detalle = DetallePedido(idPedido=id_pedido, idProducto=id_producto, cantidad=cantidad,
                                      precioUnitario=precio_unitario, fechaEntrega=fecha_entrega, estado=estado)
        session.add(nuevo_detalle)
        session.commit()
        print('Se ha agregado un nuevo detalle de pedido')

    @staticmethod
    def modificar_detalle_pedido(session, id_pedido, id_producto, **kwargs):
        detalle = session.query(DetallePedido).filter_by(idPedido=id_pedido, idProducto=id_producto).first()
        if detalle:
            for key, value in kwargs.items():
                setattr(detalle, key, value)
            session.commit()
            print('Detalle de pedido actualizado')
        else:
            print('Detalle de pedido no encontrado')

    @staticmethod
    def eliminar_detalle_pedido(session, id_pedido, id_producto):
        detalle = session.query(DetallePedido).filter_by(idPedido=id_pedido, idProducto=id_producto).first()
        if detalle:
            session.delete(detalle)
            session.commit()
            print('Detalle de pedido eliminado')
        else:
            print('Detalle de pedido no encontrado')

class Pago(Base):
    __tablename__ = 'pago'
    idpago = Column(Integer, primary_key=True)
    idpedido = Column(Integer, ForeignKey('pedido.idpedido'))
    montopagado = Column(Integer, nullable=False)
    deudaactual = Column(Integer, nullable=False)
    estado = Column(Integer, default=1)
    fecharegistro = Column(TIMESTAMP, nullable=False, server_default=func.current_TIMESTAMP()) 
    fechaactualizacion = Column(TIMESTAMP)


    @staticmethod
    def mostrar_todos_pagos(session):
        pagos = session.query(Pago).all()
        for pago in pagos:
            print("ID de Pago:", pago.idpago)
            print("ID de Pedido:", pago.idpedido)
            print("Monto Pagado:", pago.montopagado)
            print("Deuda Actual:", pago.deudaactual)
            print("Estado:", pago.estado)
            print("Fecha de Registro:", pago.fecharegistro)
            print("Fecha de Actualización:", pago.fechaactualizacion)
            print("-------------------------------------------")

    @staticmethod
    def mostrar_pago_por_id(session, id_pago):
        pago = session.query(Pago).filter_by(idPago=id_pago).first()
        if pago:
            print('PAGO ENCONTRADO')
            print("ID de Pago:", pago.idpago)
            print("ID de Pedido:", pago.idpedido)
            print("Monto Pagado:", pago.montopagado)
            print("Deuda Actual:", pago.deudaactual)
            print("Estado:", pago.estado)
            print("Fecha de Registro:", pago.fecharegistro)
            print("Fecha de Actualización:", pago.fechaactualizacion)
            print("-------------------------------------------")
        else:
            print('No existe el pago mencionado')

    @staticmethod
    def agregar_pago(session, id_pedido, monto_pagado, deuda_actual, estado=1):
        nuevo_pago = Pago(idpedido=id_pedido, montopagado=monto_pagado, deudaactual=deuda_actual, estado=estado)
        session.add(nuevo_pago)
        session.commit()
        print('Se ha agregado un nuevo pago')

    @staticmethod
    def modificar_pago(session, id_pago, **kwargs):
        pago = session.query(Pago).filter_by(idpago=id_pago).first()
        if pago:
            for key, value in kwargs.items():
                setattr(pago, key, value)
            session.commit()
            print('Pago actualizado')
        else:
            print('Pago no encontrado')

    @staticmethod
    def eliminar_pago(session, id_pago):
        pago = session.query(Pago).filter_by(idpago=id_pago).first()
        if pago:
            session.delete(pago)
            session.commit()
            print('Pago eliminado')
        else:
            print('Pago no encontrado')