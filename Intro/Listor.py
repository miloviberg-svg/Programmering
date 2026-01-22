students = []
"""
print(students[1])
students.append("Johan")
print(students)
students.insert(1, "Erik")
print(students)

students.remove("johan")
print(students)
students.pop(1)
print(students)
"""

# används för att komma åt innehållet
for student in students:
    print(student)

    numbers = [10, 77, 53, 24]
    
for number in numbers:
    number += 10

# används för att ändra innehållet
    for i in range(len(numbers)):
        numbers[i] += 10

    print (numbers)