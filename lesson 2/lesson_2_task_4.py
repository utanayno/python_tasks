def fizz_buzz(number):
    for number in range(1, number+1):
        if (number % 5 == 0) and (number % 3 == 0):
            print("FizzBuzz")
        elif (number % 3 == 0):
            print("Fizz")
        elif (number % 5 == 0):
            print("Buzz")
        else: 
            print(number)
number = int(input("Введите число: "))
fizz_buzz(number)