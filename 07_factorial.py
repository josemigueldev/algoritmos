# Factorial de un número

def factorial(num):
    result = 1

    if num < 0:
        return "Sorry, factorial does not exist for negative numbers"
    elif num == 0:
        return "The factorial of 0 is 1"
    else:
        for i in range(1, num + 1):
            result = result * i
        return f"The factorial of {num} is {result}"


if __name__ == "__main__":
    number = int(input("Enter a number: "))
    print(factorial(number))
