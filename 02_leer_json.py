import json

def cargar_datos(ruta):
    with open(ruta) as contenido:
        # cursos es una lista de diccionarios
        cursos = json.load(contenido)
        for curso in cursos:
            for clave, valor in curso.items():
                print(f"{clave}: {valor}")


if __name__ == "__main__":
    ruta = "datos/cursos.json"
    cargar_datos(ruta)

"""
Diferencia entre load() y loads()
load() es para deserializar un archivo mientras que loads() para un string

WITH es un administrador de contexto
Se utiliza un administrador de contexto para que los recursos necesarios del
programa se creen y se limpien correctamente.

Por lo general se usa para  abrir un archivo o una conexion a una base de datos,
procesar su contenido y cerciorarse de cerrarlo.
"""
