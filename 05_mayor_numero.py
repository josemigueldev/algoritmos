# Obtener el mayor numero de tres numeros

def largest_number(num1, num2, num3):
    if (num1 >= num2) and (num1 >= num3):
        return num1
    elif (num2 >= num1) and (num2 >= num3):
        return num2
    else:
        return num3


def largest_number_two(*args):
    numbers = []

    for number in args:
        numbers.append(number)

    return max(numbers)


if __name__ == "__main__":
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    num3 = float(input("Enter third number: "))
    numbers = [num1, num2, num3]

    print(largest_number(num1, num2, num3))
    print(largest_number_two(num1, num2, num3))
    print(largest_number_two(*numbers))
