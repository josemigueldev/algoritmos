# Programa para sumar n numeros naturales

def sum_natural_numbers(num):
    if num < 0:
        return "Enter a positive number"
    else:
        accum = 0
        while (num > 0):
            accum += num
            num -= 1
        return f"The sum is: {accum}"


if __name__ == "__main__":
    num = int(input("Enter a number: "))
    print(sum_natural_numbers(num))
