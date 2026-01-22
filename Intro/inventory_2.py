backpack = []

while True:
    print("Vad vill du göra?")
    print("1. Visa Ryggsäcken")
    print("2. Plocka upp något")
    print("3. Släppa något i ryggsäcken")
    print("4. Byta plats i ryggsäcken")
    print("q. Stänga av")

    choice = input()

    if choice == "1":
        for item in backpack:
            print(item)
    
    elif choice == "2":
        item = input("Vad vill du plocka upp? ")
        backpack.append(item)
    elif choice == "3":
        print(backpack)
        item = input("Vad vill du släppa? ")

        try:
            backpack.remove(item)
            print("tog bort den")
        except:
            print("Hittade den inte")
    elif choice == "4":
        print("välj genom siffrorna 0 - slutet av listan")
        print(backpack)
        Objekt_1 = int(input("första numret: "))
        Objekt_2 = int(input("andra numret: "))
        backpack[Objekt_1], backpack[Objekt_2] = backpack[Objekt_2], backpack[Objekt_1]
        print(backpack)
    elif choice == "q":
        break
    else:
        print("Ogiltigt Svar")
    
    input("\nTryck enter för att fortsätta...")