# Mostrar el calendario de un año y un mes en especifico
import calendar

def view_calendar(year, month):
    return calendar.month(year, month)

if __name__ == "__main__":
    year = int(input("Enter a year: "))
    month = int(input("Enter a month: "))
    print(view_calendar(year, month))

"""
Enter a year: 1988
Enter a month: 6

     June 1988
Mo Tu We Th Fr Sa Su
       1  2  3  4  5
 6  7  8  9 10 11 12
13 14 15 16 17 18 19
20 21 22 23 24 25 26
27 28 29 30
"""
