names = ['Abdul Ahad', 'Jiya','Hasan Ali', 'Jani' ,'Hashmi', 'Naceed','Usama', 'Asad']
print(names)
print(names[0])
print(names[1])
print(names[-1])
print(names[2:])
print(names[:2])
print(names[3:7])

# program to find the largest number in List

numbers = [2,5,6,2,8,3,80]
large_number=numbers[0]

for item in numbers:
    if item>large_number:
        large_number = item

print(f"The Large number is: {large_number}")



