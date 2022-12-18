marks = [22, 78, 90, 65, 89, 90, 77]
print(marks)
marks.append(1990)
print(marks)

marks.insert(3, 900)
print(marks)
marks.remove(900)
print(marks)

marks.pop()
print(marks)
# print(marks.index(8))

print(50 in marks)
print(1990 in marks)
print(22 in marks)
print(marks.count(9))
print(marks.count(5))
marks.sort()
marks.reverse()
print(marks)


marks2 = marks.copy()
marks.append(400)
print(marks)
print(marks2)


# remove duplicate tha number in list

D = [1, 2,1, 1, 6]
unique = []
for number in D:
     if number not in unique:
         unique.append(number)

print(unique)
