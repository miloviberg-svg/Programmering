zoo = {
    "lejon" : {"territory" : "subtropiska zonen", "species" : "kattdjur", "name" : "Mufasa", "happiness" : 100, "age" : 7},
    "varg" : {"territory" : "tempererade zonen", "species" : "hunddjur", "name" : "Wolfie", "happiness" : 40, "age" : 4},
    "schimpans" : {"territory" : "tropiska zonen", "species" : "människoapa", "name" : "Elias", "happiness" : 60, "age" : 5},
    "pigghaj" : {"territory" : "tempererade zonen", "species" : "haj", "name" : "leo", "happiness" : 75, "age" : 27},
    "nätgiraff" : {"territory" : "subtopiska zonen", "species" : "giraff", "name" : "Ponzo", "happiness" : 70, "age" : 19},
    "brunbjörn" : {"territory" : "tempererade zonen", "species" : "björn", "name" : "Cupcake", "happiness" : 10, "age" : 17},
    "jaguar" : {"territory" : "tropiska zonen", "species" : "jaguar", "name" : "lebron", "happiness" : 90, "age" : 9},
    "pingvin" : {"territory" :"polar zonen", "species" : "flygoförmögen havsfågel", "name" : "pingu", "happiness" : 100, "age" : 5},
    "isbjörn" : {"territory" : "polar zonen", "species" : "isbjörn", "name" : "princess", "happiness" : 12, "age" : 3}
}

while True:
    print("Vad vill du göra?")
    print("1. visa områden")
    print("2. lägga till djur")
    print("3. hälsa på djur")
    print("4. visa rapport")

    choice = input()

    if choice == "1":
        print("1 = polar zonen")
        print("2 = tempererade zonen"), 
        print("3 = subtropiska zonen")
        print("4 = tropiska zonen")

        t_choice = input()

        if t_choice == "1":
            for animal in zoo.keys():
                if zoo[animal]["territory"] == "polar zonen":
                    print(animal)
            
        elif t_choice == "2":
            for animal in zoo.keys():
                if zoo[animal]["territory"] == "tempererade zonen":
                    print(animal)

        elif t_choice == "3":
            for animal in zoo.keys():
                if zoo[animal]["territory"] == "subtropiska zonen":
                    print(animal)
            
        elif t_choice == "4":
            for animal in zoo.keys():
                if zoo[animal]["territory"] == "tropiska zonen":
                    print(animal)
        else:
            print("fuck you, gör rätt")

    elif choice == "2": 
        print("vilket djur vill du lägga till?")
        add = input()
        print("vilket område?")
        add_t = input()
        print("vilken art?")
        add_s = input()
        print("vad heter djuret?")
        add_n = input()
        print("hur glad är djuret?")
        add_h = int(input())
        print("hur gammal är djuret?")
        add_a = int(input())
        zoo[add] = {"territory" : add_t, "species" : add_s, "name" : add_n, "happiness" : add_h, "age" : add_a}
    
    elif choice == "3":
        print("1. polar zonen")
        print("2. tempererade zonen")
        print("3. subtropiska zonen")
        print("4. tropiska zonen")

        t_choice_2 = input()

        if t_choice_2 == "1":
            t_choice_3 = "polar zonen"
        elif t_choice_2 == "2":
            t_choice_3 = "tempererade zonen"
        elif t_choice_2 == "3":
            t_choice_3 = "subtropiska zonen"
        elif t_choice_2 == "4":
            t_choice_3 = "tropiska zonen"
        else:
            print("fuck you!")


        
        print("vad vill du göra?")
        print("1. mata")
        print("2. lek")
        print("3. städa")
        
        a_choice = input()

        if a_choice == "1":
            for animal in zoo.keys():
                if zoo[animal]["territory"] == t_choice_3:
                    zoo[animal]["happiness"] += 4

        elif a_choice == "2":
            for animal in zoo.keys():
                if zoo[animal]["territory"] == t_choice_3:
                    zoo[animal]["happiness"] += 3

        elif a_choice == "3":
            for animal in zoo.keys():
                if zoo[animal]["territory"] == t_choice_3:
                    zoo[animal]["happiness"] += 2
        else:
            print("fuck you, stava rätt!")
                    
                    
    elif choice == "4":

        print(f"Det finns {len(zoo)} Djur")




    input("Tryck enter för att köra igen.")

     