try:
    user_age = int(input("Enter your age: "))
    print(user_age)
except ValueError:
    print('invaild value')
    print(ValueError)


try:
    num1 = int(input('Enter Your first number: '))
    num2 = int(input('Enter Your second number: '))
    result = num1/num2
    print(result)
except ZeroDivisionError:
    print("We can't divide by zero")