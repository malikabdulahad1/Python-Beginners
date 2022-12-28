try:
    num1 = int(input('Enter 1st number'))
    num2 = int(input('Enter 2nd number'))
    print(num1)
    print(num2)
    num3 = num1/num2
except ValueError:
    print('Invaild value')
except ZeroDivisionError:
    print('Zero can not be divided')