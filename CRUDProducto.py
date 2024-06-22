from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from OrmEstudio64 import Base, Producto

DATABASE_URL = "postgresql://postgres:1234567@localhost:5432/bdEstudio64"

engine = create_engine(DATABASE_URL)

Session = sessionmaker(bind=engine)
session = Session()


# CRUD TABLA Producto
def main_menu():
    while True:
        print("\nMenú Principal")
        print("1. Agregar Producto ")
        print("2. Ver Productos")
        print("3. Modificar Producto ")
        print("4. Eliminar Producto")
        print("5. Salir ")
      
        
        choice = input("Elige una opción (1-4): ")
        
        if choice == '1':
            descripcion = input("Descripción del producto: ")
            unidad_medida = input("Unidad de medida del producto: ")
            stock = int(input("Stock del producto: "))
            precio_base = float(input("Precio base del producto: "))
            Producto.agregar_producto(session, descripcion, unidad_medida, stock, precio_base)
            
        elif choice == '2':
            ver = input("Ingrese el id del producto o si desea ver todos los productos escriba 'todos': ")
            if ver == "todos":
                  Producto.mostrar_todos_los_productos(session)
            else:
                Producto.mostrar_producto_por_id(session, ver)       
        
        elif choice == '3':
            id_producto = input("Ingrese el id del producto que desea modificar: ")
            descripcion = input("Descripción del producto: ")
            unidad_medida = input("Unidad de medida del producto: ")
            stock = int(input("Stock del producto: "))
            precio_base = float(input("Precio base del producto: "))
            Producto.modificar_producto(session, id_producto, descripcion=descripcion, unidadmedida=unidad_medida, stock=stock, preciobase=precio_base)
        
        elif choice == '4':
            id_producto = input("Ingrese el id del producto que desea eliminar: ")
            Producto.modificar_producto(session, id_producto, estado=0)
        
        elif choice == '5':
            break
        else:
            print("Opción no válida. Por favor, elige una opción entre 1 y 4.")


if __name__ == "__main__":
    while True:
        main_menu()

session.close()