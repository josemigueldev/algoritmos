# Programa para mostrar la secuencia de Fibonacci hasta el enésimo término

def fibonacci(n):
    # agregamos los primeros dos terminos
    numbers = [0, 1]

    # comprobar si el numero de terminos es valido
    if nterms <= 0:
        print("Please enter a positive integer")
    # si solo hay un termino
    elif nterms == 1:
        print(f"Fibonacci sequence upto {n}:")
        print(numbers[0])
    # generamos la secuencia
    else:
        print(f"Fibonacci sequence upto {n}:")
        for i in range(n):
            print(numbers[i])
            nth = numbers[i] + numbers[i+1]
            numbers.append(nth)


if __name__ == "__main__":
    try:
        nterms = int(input("How many terms? "))
        fibonacci(nterms)
    except ValueError:
        print("Enter a number")
