import requests

def obtener_pokemones(url, offset=0):
    # asignamos el valor del argumento offset para listar mas pokemones
    args = {"offset": offset} if offset else {}
    peticion = requests.get(url, params=args)

    if peticion.status_code == 200:
        respuesta = peticion.json()  # devuelve un diccionario
        # obtener la llave results sino asigna una lista vacia
        datos = respuesta.get("results", [])

        if datos:  # si la lista no esta vacia
            # datos es una lista de diccionarios
            for pokemon in datos:
                print(pokemon["name"])

        continuar = input("Continuar listando? [Y/N]: ").lower()

        if continuar == "y":
            obtener_pokemones(url, offset=offset+20)


if __name__ == "__main__":
    # esta url devuelve los 20 primeros pokemones
    url = "https://pokeapi.co/api/v2/pokemon-form/"
    obtener_pokemones(url)
