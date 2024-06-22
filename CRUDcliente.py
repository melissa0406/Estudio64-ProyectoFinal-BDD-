from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from OrmEstudio64 import Base, Cliente 
# Configuración de la base de datos
DATABASE_URL = "postgresql://postgres:1234567@localhost:5432/bdEstudio64"

engine = create_engine(DATABASE_URL)

Session = sessionmaker(bind=engine)
session = Session()


# CRUD TABLA CIENTE 

def main_menu():
    while True:
        print("\nMenú Principal")
        print("1. Agregar Cliente ")
        print("2. Ver Clientes")
        print("3. Modificar Cliente ")
        print("4. Eliminar Cliente")
        print("5. Salir ")
      
        
        choice = input("Elige una opción (1-4): ")
        
        if choice == '1':
            n= input("nombre: ")
            ap= input("apellido paterno: ")
            am= input("Apellido materno: ")
            c= input("Celular: ")
            Cliente.agregar_cliente(session,n,ap,am,c)
            
            
        elif choice == '2':
            ver= input("Ingrese el id del cliente o si desea ver a todos los cliente escriba todos ")
            if ver=="todos":
                  Cliente.mostrar_todos_los_clientes(session)
            else:
                Cliente.mostrar_cliente_por_id(session,ver)       
        
        elif choice == '3':
            idC=input("Ingrese el id del cliente que desea modificar")
            n= input("nombre: ")
            ap= input("apellido paterno: ")
            am= input("Apellido materno: ")
            c= input("Celular: ")
            Cliente.modificar_cliente(session, idC, nombres=n,apellidopaterno=ap, apellidomaterno=am ,celular=c)
        elif choice == '4':
            idC=input("Ingrese el id del cliente que desea eliminar ")
            Cliente.modificar_cliente(session, idC, estado=0)
        
        elif choice == '5':
            break
        else:
            print("Opción no válida. Por favor, elige una opción entre 1 y 4.")



if __name__ == "__main__":
    while True:
        main_menu()


session.close()