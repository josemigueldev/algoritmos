# Programa para mostrar las potencias de un numero dado y la cantidad de
# terminos a mostrar, usar una funcion anonima.

if __name__ == "__main__":
    base = int(input("Enter a base: "))
    terms = int(input("How many terms? "))

    result = list(map(lambda x: base ** x, range(terms)))

    print("The total terms are:", terms)

    for i in range(terms):
        print(f"{base} raised to power {i} is {result[i]}")
