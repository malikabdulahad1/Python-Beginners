a = input("Enter your weight: ")
unit = input("Enter Your weight in (L)bs or (K)g: ")

weight = int(a)

if unit=='L' or unit=='l':
    converted = weight*0.45
    print(f"Your are {converted} kilos")
elif unit=='K' or unit == 'k':
    converted = weight/0.45
    print(f"you are {converted} pound")
else:
    print('Enter invaild character')
