from sqlalchemy import select
from sqlalchemy.orm import Session

from modelos import Libro


def listar_libros(
    session: Session
) -> list[Libro]:
    """
    Recupera todos los libros ordenados alfabéticamente por su título.
    """
    stmt = select(Libro).order_by(Libro.titulo)
    return list(session.scalars(stmt).all())


def buscar_libro_por_id(
    session: Session,
    id_libro: int
) -> Libro | None:
    """
    Busca un libro por su clave primaria utilizando session.get().
    Devuelve el objeto Libro o None si no existe.
    """
    return session.get(Libro, id_libro)
