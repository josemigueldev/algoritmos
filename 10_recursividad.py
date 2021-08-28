# Programa para mostrar la secuencia de Fibonacci de forma recursiva

def recur_fibo(n):
    if n <= 1:
        return n
    else:
        return recur_fibo(n - 1) + recur_fibo(n - 2)


if __name__ == "__main__":
    try:
        nterms = int(input("How many terms? "))
        if nterms <= 0:
            print("Please enter a positive integer")
        else:
            print(f"Fibonacci sequence upto {nterms}:")
            for i in range(nterms):
                print(recur_fibo(i))
    except ValueError:
        print("Enter a number")
