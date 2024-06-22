from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker


# Configuración de la base de datos
DATABASE_URL = "postgresql://postgres:1234567@localhost:5432/bdEstudio64"

# Crear el motor de la base de datos
engine = create_engine(DATABASE_URL)


# Crear una conexión
with engine.connect() as connection:
    # Comprobar la conexión (ejemplo de consulta)
    try:
        result = connection.execute(text('SELECT 1'))
        print("Conexión exitosa:", result.scalar())
    except Exception as e:
        print("Error al conectar a la base de datos:", str(e))
