from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from OrmEstudio64 import Base, Empleado


DATABASE_URL = "postgresql://postgres:1234567@localhost:5432/bdEstudio64"

engine = create_engine(DATABASE_URL)

Session = sessionmaker(bind=engine)
session = Session()



def mostrar_menu1():
    print("Menú de Empleados")
    print("1. Mostrar todos los empleados")
    print("2. Mostrar empleado por ID")
    print("3. Agregar empleado")
    print("4. Modificar empleado")
    print("5. Eliminar empleado")
    print("6. Salir")
    choice = input("Elige una opción (1-6): ")
    return choice

if __name__ == "__main__":
    while True:
        choice = mostrar_menu1()

        if choice == '1':
            Empleado.mostrar_todos_los_empleados(session)

        elif choice == '2':
            id_empleado = int(input("Ingrese el ID del empleado: "))
            Empleado.mostrar_empleado_por_id(session, id_empleado)

        elif choice == '3':
            id_oficina = int(input("Ingrese el ID de la oficina del empleado: "))
            nombre = input("Ingrese el nombre del empleado: ")
            fecha_nacimiento = input("Ingrese la fecha de nacimiento del empleado (YYYY-MM-DD): ")
            nombre_usuario = input("Ingrese el nombre de usuario del empleado: ")
            passw = input("Ingrese la contraseña del empleado: ")
            password = passw.encode().hex()
            Empleado.agregar_empleado(session,id_oficina, nombre,fecha_nacimiento,nombre_usuario,password)

        elif choice == '4':
            id_empleado = int(input("Ingrese el ID del empleado que desea modificar: "))
            nom = input("Ingrese el nombre del empleado: ")
            fecha_nacimiento = input("Ingrese la fecha de nacimiento del empleado (YYYY-MM-DD): ")
            nombre_usuario = input("Ingrese el nombre de usuario del empleado: ")
            passw = input("Ingrese la contraseña del empleado: ")
            password = passw.encode().hex()
            Empleado.modificar_empleado(session, id_empleado, nombre=nom, fechanacimiento = fecha_nacimiento, nombreusuario=nombre_usuario,password=password)

        elif choice == '5':
            id_empleado = int(input("Ingrese el ID del empleado que desea eliminar: "))
           
            Empleado.modificar_empleado(session, id_empleado, estado=0)

        elif choice == '6':
            print("Saliendo del programa...")
            session.close()
            exit()

        else:
            print("Opción no válida. Inténtalo de nuevo.")
