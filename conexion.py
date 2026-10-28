from sqlalchemy import Engine, create_engine, text
from sqlalchemy.orm import sessionmaker

from configuracion import obtener_url_conexion


def crear_engine(echo: bool = True) -> Engine:
    """
    Crea y devuelve el Engine de SQLAlchemy conectado a PostgreSQL.
    """
    url = obtener_url_conexion()
    return create_engine(url, echo=echo)


# Engine global con echo=True para observar el SQL generado (Paso 6)
engine = crear_engine(echo=True)

# Factoría de sesiones vinculada al Engine
SessionLocal = sessionmaker(bind=engine)


def comprobar_conexion(motor: Engine = engine) -> bool:
    """
    Comprueba la conexión con la base de datos biblioteca.
    """
    with motor.connect() as conexion:
        resultado = conexion.execute(
            text("SELECT current_database(), current_user")
        ).one()
        print(f"Conexión correcta a la base de datos '{resultado[0]}' con el usuario '{resultado[1]}'.")
    return True
