import math


def square(side):
    print("Площадь квадрата равна: ", rounded_side*rounded_side)
side = float(input("Введите сторону квадрата: "))
rounded_side = math.ceil(side)
square(side)