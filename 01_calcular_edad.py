# Calcular la edad de una persona pasando como parametro la fecha de nacimiento
from datetime import date

def calcular_edad(fecha_nacimiento):
    # obtenemos la fecha de hoy
    hoy = date.today()  # 2021-08-22 (ejemplo)

    try:
        # sustituimos el año de nacimiento por el actual para comparar solo
        # los meses y los dias
        cumpleanios = fecha_nacimiento.replace(year=hoy.year)
    except ValueError:
        # En caso de que la fecha de nacimiento es 29 de febrero y el año
        # actual no es bisiesto le restamos uno al dia de nacimiento para que
        # quede en 28
        cumpleanios = fecha_nacimiento.replace(year=hoy.year, day=fecha_nacimiento.day - 1)

    # Calculo final
    if cumpleanios > hoy:  # aun no cumple años actualmente
        return hoy.year - fecha_nacimiento.year - 1
    else:  # ya cumplio años actualmente
        return hoy.year - fecha_nacimiento.year


print(calcular_edad(date(1988, 6, 6)))  # 33
print(calcular_edad(date(2004, 2, 29)))  # 17 (2004 es bisiesto)
