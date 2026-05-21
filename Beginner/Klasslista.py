with open("students.txt", "r") as file:
    lines = file.read().split("\n")
    students = lines

while True:

    students = [
        {"namn" : "Carl Carlsson", "år" : 1}
    ]
    print ("1. lägg till elev \n2. visa lista \n3. visa elev per läsår \n4. ta bort elerv \n5. quit")

    choice = int(input())
    if choice == 1:
        print("vem vill du lägga till?")
        new_student = input()
        with open("students.txt", "w") as file:
            students.append(new_student)
            file.write("\n".join(students))

    with open('students.txt', 'r', encoding="utf-8") as file:
        students = file.read().split('\n')

    if choice == 2:
        #with open("students.txt", "r") as file:
        #    lines = file.read().split("\n")
        #    students = lines
        #    print(students)
        for student in students:
            print('-', student["namn"])


    elif choice == 3:
        pass

    elif choice == 4:
        remove_student = input("Vem vill du ta bort? ")

        if remove_student in students:
            students.remove(remove_student)

            with open("student.txt", "w") as file:
                file.write("\n".join(students))

            print(f"{remove_student} har tagits bort.")
        else:
            print("Studenten finns inte i listan.")

    elif choice == 5:
        break

    else:
        break

    input("\nTryck enter för att fortsätta...")