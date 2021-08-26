# Mostrar si un numero es primo o NO

def prime_number(num):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                return f"{num} is not a prime number"
        return f"{num} is a prime number"
    else:
        return "enter a number greater than 1"


if __name__ == "__main__":
    number = int(input("Enter a number: "))
    print(prime_number(number))
