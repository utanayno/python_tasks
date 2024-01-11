x = int(input("Введите сумму вклада: "))
y = int(input("Введите количество лет: "))
def bank(x,y):
    for i in range(y):
        x = (x + (x / 10))
    return x
print(bank(x,y))