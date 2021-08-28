# Programa para mostrar el factorial de un numero proporcionado por el usuario

def factorial(num):
    fact = 1

    if num < 0:
        return "Sorry, factorial does not exist for negative numbers"
    elif num == 0:
        return f"The factorial of {num} is {fact}"
    else:
        for i in range(1, num + 1):
            fact = fact * i
        return f"The factorial of {num} is {fact}"


def recur_fact(num):
    if num < 0:
        return -1
    if (num == 1) or (num == 0):
        return 1
    else:
        return num * recur_fact(num - 1)


if __name__ == "__main__":
    num = int(input("Enter a number: "))
    print(factorial(num))
    print(recur_fact(num))
