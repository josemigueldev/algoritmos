# Programa para buscar numeros divisibles en una lista por otro numero

def divisible_numbers(num, numbers):
    result = list(filter(lambda x: x % num == 0, numbers))
    return f"Numbers divisible by {num} are: {result}"


if __name__ == "__main__":
    numbers = [12, 65, 54, 39, 102, 339, 221]
    num = int(input("Enter a number: "))

    print(divisible_numbers(num, numbers))

"""
Enter a number: 13
Numbers divisible by 13 are: [65, 39, 221]
"""
