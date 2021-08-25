"""
Calcular si un año es bisiesto
==============================
Es bisiesto si es divisible entre 4 pero no es divisible entre 100 pero si
puede ser divisible entre 400

Desde un enfoque algoritmico, se consideran las proposiciones:
p: es divisible entre 4
q: es divisible entre 100
r: es divisible entre 400

Formula: p and (not(q) or r)
"""

def es_bisiesto(anio):
    if (anio % 4) == 0:
        if (anio % 100) == 0:
            if (anio % 400) == 0:
                return f"{anio} Si es una año bisiesto"
            else:
                return f"{anio} No es una año bisiesto"
        else:
            return f"{anio} Si es un año bisiesto"
    else:
        return f"{anio} No es un año bisiesto"

def es_bisiesto_proposiciones(anio):
    divisible_4 = anio % 4 == 0
    divisible_100 = anio % 100 == 0
    divisible_400 = anio % 400 == 0

    return divisible_4 and (not(divisible_100) or divisible_400)


if __name__ == "__main__":
    anio = int(input("Ingrese una año: "))
    print(es_bisiesto(anio))
    print(es_bisiesto_proposiciones(anio))
