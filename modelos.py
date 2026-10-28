from decimal import Decimal
from sqlalchemy import Numeric, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    """
    Clase base declarativa para los modelos ORM de SQLAlchemy.
    """
    pass


class Libro(Base):
    """
    Modelo ORM que representa la tabla 'libros' de la base de datos biblioteca.
    """
    __tablename__ = "libros"

    id_libro: Mapped[int] = mapped_column(primary_key=True)
    isbn: Mapped[str] = mapped_column(String(20), unique=True, nullable=False)
    titulo: Mapped[str] = mapped_column(String(200), nullable=False)
    precio: Mapped[Decimal] = mapped_column(Numeric(10, 2), nullable=False)

    def __repr__(self) -> str:
        return (
            f"Libro(id_libro={self.id_libro}, "
            f"titulo='{self.titulo}', "
            f"precio={self.precio})"
        )
