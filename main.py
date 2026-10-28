from sqlalchemy.orm import Session

from conexion import comprobar_conexion, engine
from consultas import buscar_libro_por_id, listar_libros


def main() -> None:
    print("============================================================")
    print("1. COMPROBACIÓN DE LA CONEXIÓN CON BIBLIOTECA")
    print("============================================================")
    comprobar_conexion(engine)

    print("\n============================================================")
    print("2. LISTADO DE TODOS LOS LIBROS (ordenados por título)")
    print("============================================================")
    with Session(engine) as session:
        libros = listar_libros(session)
        for libro in libros:
            print(libro)

    print("\n============================================================")
    print("3. BÚSQUEDA DE LIBRO POR IDENTIFICADOR")
    print("============================================================")
    with Session(engine) as session:
        id_existente = 1
        libro_encontrado = buscar_libro_por_id(session, id_existente)
        print(f"Búsqueda con ID existente ({id_existente}): {libro_encontrado}")

        id_inexistente = 999999
        libro_no_encontrado = buscar_libro_por_id(session, id_inexistente)
        print(f"Búsqueda con ID inexistente ({id_inexistente}): {libro_no_encontrado}")


if __name__ == "__main__":
    main()
