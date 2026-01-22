
shop = {
    "äpple" : { "price" : 5, "amount" : 10},
    "mjölk" : { "price" : 10, "amount" : 20}, 
    "wddamelon" : {"price" : 15, "amount" : 15}
}

sales = []

print("Välkommen till Butikshanteraren 3000")
print('Inloggad som Butiksägare')
while True:
    print("Vad vill du göra?")
    print("1. Visa alla varor")
    print("2. Lägg till en ny vara")
    print("3. Ändra priset på vara")
    print("4. Fylla på vara")
    print("5. Sälja en vara")
    print("6. Visa total intäkter")
    print("q. Stänga av")

    choice = input()

    if choice == "1":
        for item, price in shop.items():
            print(item.ljust(12), price["price"],"kr", price["amount"],"st")

    elif choice == "2":
        print("Vad vill du lägga till?")
        lägga_till = input()
        print("hur mycket ska det kosta?")
        lägga_till_pris = int(input())
        print("Hur mycket finns det av varan på lagret?")
        lägga_till_lager = int(input())
        shop[lägga_till] = {"price" : lägga_till_pris, "amount" : lägga_till_lager}
    elif choice == "3":
        print("vilken vara vill du ändra pris på?")
        nytt_vara = input()
        if nytt_vara in shop:
            print("vad vill du att varan ska kosta")
            try:
                nytt_pris = int(input())
                shop[nytt_vara]["price"] = nytt_pris
            except:
                print("Fel! Det där var ett ogiltigt pris")
        else:
            print("Fuck you, gör rätt!")
    elif choice == "4":
        print("vilken vara vill du fylla på?")
        lager_vara = input()
        if lager_vara in shop:
            print("hur många av varan ska fyllas på?")
            try:
                Påfyllning = int(input())
                shop[lager_vara]["amount"] += Påfyllning
            except:
                print("Fel! Det där var ett ogiltigt pris")
        else:
            print("Fuck you, gör rätt!")
    elif choice == "5":
        print("Vad vill du sälja?")
        vara = input()
        if vara in shop:
            print("hur många vill du sälja?")
            try:
                säljning = int(input())
                shop[vara]["amount"] -= säljning
            except:
                print("Fel! Det där var ett ogiltigt pris")
        else:
            print("Fuck you, gör rätt!")
            
    elif choice == "6":
        pass
        # din kod här
    elif choice == "q":
        break
    else:
        print("Ogiltigt Svar")
    
    input("\nTryck enter för att fortsätta...")