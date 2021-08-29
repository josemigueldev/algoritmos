# Programa para comprobar si un numero es un numero armstrong o no
"""
Un numero narcisista es aquel que es igual a la suma de sus dígitos elevados a
la potencia de su número de cifras.

153 = 1^3 + 5^3 + 3^3
8208 = 8^4 + 2^4 + 0^4 + 8^4
"""

def armstrong_number(num):
    numbers = [int(i) for i in str(num)]
    length = len(numbers)
    accum = 0

    for i in numbers:
        accum += i ** length
        if accum > num:
            break

    if accum == num:
        return f"{num}, is an Armstrong number"
    else:
        return f"{num}, is not an Armstrong number"


if __name__ == "__main__":
    num = int(input("Enter a number: "))
    print(armstrong_number(num))
