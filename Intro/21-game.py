number = 0
print("välkommen till 21 game")

last_picked_1 = None
last_picked_2 = None

while True:

    while True:
        print ("spelare ett skriver ett nummer mellan 1 och 2")
        choice = int(input())
        if choice > 2 or choice < 1:
            print ("Ogiltig nummer, starta om")
            continue
        else:
            if choice == last_picked_1:
                print("du kan inte skriva samma nummer som innan")
                continue
            number = number + choice
            print (number)
            last_picked_1 = choice
            break
    if number == 21:
        print ("spelare 1 vann")
        break
    if number > 21:
        print ("spelare 2 vann")
        break

    while True:            
        print("spelar två skriver ett nummer mellan 1 och 2")
        choice_2 = int(input())
    
        if choice_2 > 2 or choice < 1:
            print ("ogiltigt nummer, starta om")
            continue
        else:
            if choice_2 == last_picked_2:
                print("du kan inte skriva samma nummer som innan")
                continue
            number = number + choice_2
            print (number)
            last_picked_2 = choice_2
            break
                
    if number == 21:
        print ("spelare 2 vann")
        break
    if number > 21:
        print ("spelare 1 vann")
        break