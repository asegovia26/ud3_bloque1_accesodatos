import os


def obtener_url_conexion() -> str:
    """
    Construye y devuelve la URL de conexión para SQLAlchemy
    a partir de las variables de entorno.
    """
    host = os.getenv("DB_HOST", "localhost")
    port = os.getenv("DB_PORT", "5432")
    dbname = os.getenv("DB_NAME", "biblioteca")
    user = os.getenv("DB_USER", "alumno")
    password = os.getenv("DB_PASSWORD", "")

    if password:
        return f"postgresql+psycopg://{user}:{password}@{host}:{port}/{dbname}"
    return f"postgresql+psycopg://{user}@{host}:{port}/{dbname}"
