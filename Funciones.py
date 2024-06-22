from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from OrmEstudio64 import Base, Cliente, Empleado, Producto, Pedido, Credito, DetallePedido, Pago



 # Configuración de la base de datos
DATABASE_URL = "postgresql://postgres:1234567@localhost:5432/bdEstudio64"

# Crear el motor de la base de datos
engine = create_engine(DATABASE_URL)

# Crear las tablas en la base de datos si no existen
Base.metadata.create_all(engine)

# Crear una sesión
Session = sessionmaker(bind=engine)
session = Session()

#FUNCION 1 
# CUANTOS PEDIDOS TIENE UN EMPLEADO 

def obtener_pedidos_entregados_por_empleado(session):
   
    pedidos_entregados = session.query(Empleado.idempleado, Empleado.nombre, func.count(Pedido.idpedido).label('cantidad_pedidos_entregados')) \
        .join(Pedido, Empleado.idempleado == Pedido.idempleado) \
        .filter(Pedido.estado == 1) \
        .group_by(Empleado.idempleado, Empleado.nombre) \
        .all()
    if pedidos_entregados:
         print("Pedidos Entregados por Empleado:")
         for empleado_id, empleado_nombre, cantidad_pedidos_entregados in pedidos_entregados:
            print(f"ID Empleado: {empleado_id}, Nombre: {empleado_nombre}, Pedidos: {cantidad_pedidos_entregados}")
    else:
         print("No se encontraron pedidos entregados por empleado.")


## obtener_pedidos_entregados_por_empleado(session)


# FUNCION 2 
# cuanto credito le queda a un cliente segun todos los pedidos que ha realizado 
def calcular_credito_restante(session,id_cliente):
    # Obtener el cliente
    cliente = session.query(Cliente).filter_by(idcliente=id_cliente).first()
    if not cliente:
        print("Cliente no encontrado")
        return

    # Obtener el crédito del cliente
    credito = session.query(Credito).filter_by(idcredito=cliente.idcredito, estado=1).first()
    if not credito:
        print("Crédito no encontrado para el cliente")
        return

    # Obtener los pedidos del cliente
    pedidos = session.query(Pedido).filter_by(idcliente=id_cliente).all()
    if not pedidos:
        print("No se encontraron pedidos para el cliente")
        return

    # Calcular el total de todos los pedidos entregados
    total_pedidos = 0
    for pedido in pedidos:
        if pedido.estado == 1:  # Consideramos solo los pedidos entregados
            detalles = session.query(DetallePedido).filter_by(idpedido=pedido.idpedido).all()
            for detalle in detalles:
                total_pedidos += detalle.cantidad * detalle.preciounitario

    # Calcular el crédito restante
    credito_restante = credito.creditoactual - total_pedidos
    print("El credito restante actual es: ", credito_restante)

    # Actualizar el crédito actual del cliente en la base de datos
    # credito.creditoactual = credito_restante
     
    session.commit()    
    print(f"Cliente {cliente.nombres} {cliente.apellidopaterno}")
    print("su credito inicial es : ", credito.creditoinicial)
    print(f"El crédito restante del cliente {cliente.nombres}  es: {credito_restante}")

# Ejemplo de uso
## x= input("De que cliente le gustaria revisar su credito actual despues de todos sus pedidos")

## calcular_credito_restante(session, x)





#FUNCION 3 
## calcular la deudatotal, el total del monto pagado y la deuda actual que tiene todos los clientes separando sus pedidos


def obtener_deudas_y_pagos_por_cliente(session):
    # Obtener todos los clientes
    clientes = session.query(Cliente).all()

    for cliente in clientes:
        print(f"\nCliente: {cliente.nombres} {cliente.apellidopaterno} {cliente.apellidomaterno}")

        # Obtener los pedidos del cliente
        pedidos = session.query(Pedido).filter_by(idcliente=cliente.idcliente).all()

        for pedido in pedidos:
            # Calcular deuda total del pedido
            total_deuda_pedido = session.query(func.sum(DetallePedido.cantidad * DetallePedido.preciounitario)) \
                                        .filter_by(idpedido=pedido.idpedido).scalar() or 0

            # Calcular monto total pagado y deuda actual del pedido
            total_pagado = session.query(func.sum(Pago.montopagado)).filter_by(idpedido=pedido.idpedido).scalar() or 0
            # deuda_actual = session.query(func.sum(Pago.deudaactual)).filter_by(idpedido=pedido.idpedido).scalar() or 0
            
            deuda_actual=total_deuda_pedido-total_pagado

            print(f"  Pedido ID: {pedido.idpedido}")
            print(f"    Total Deuda: {total_deuda_pedido}")
            print(f"    Monto Pagado: {total_pagado}")
            print(f"    Deuda Actual: {deuda_actual}")
            print(f"    Estado del Pedido: {'Valido' if pedido.estado == 1 else 'Cancelado'}")

# Llamar a la función para obtener y mostrar los detalles
obtener_deudas_y_pagos_por_cliente(session)


session.close()