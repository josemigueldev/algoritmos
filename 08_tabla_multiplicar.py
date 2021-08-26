# Mostrar la tabla de multiplicar de un número dado

def multiplication_table(num):
    for i in range(1, 13):
        print(f"{num} x {i} = {num * i}")


if __name__ == "__main__":
    number = int(input("Display multiplication table of? "))
    multiplication_table(number)
