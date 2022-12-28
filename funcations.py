# function is a container that contains a few lines of code that perform specific task

# print() and input() is a built_in function in python

def greats_user():

    print('welcome to technical encoder')


print('start')
greats_user()
greats_user()
print('end')

# parameters


def user_info(f_name, s_name):
    print(f"User name is: {f_name} {s_name}")


user_info('Abdul', 'Ahad')


# function return


def sum(num1, num2):
    result = num1+num2
    return  result

number_1=0
number_2=0
number_1 = input('Enter 1st number: ')
number_2 = input('Enter 2nd number: ')

r = sum(number_1, number_2)

print(f"Sum of two number is: {r}")





