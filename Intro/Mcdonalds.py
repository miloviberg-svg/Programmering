lista = []


print ("Vad vill du ha? hamburgare-50kr, pommes frites-25kr, läsk-20kr, milkshake-30kr, sallad 45kr, nuggets 35kr")

food = input()

if food == "hamburgare":
    print("Det blir 50kr")
    lista.append(food)
elif food == "pommes frites":
    print("Det blir 25kr")
    lista.append(food)
elif food == "läsk":
    print("det blir 20kr")
    lista.append(food)
elif food == "milkshake":
    print("Det blir 30k")
    lista.append(food)
elif food == "sallad":
    print("Det blir 45kr,")
    lista.append(food)
elif food == "nuggets":
    print("Det blir 35kr")
    lista.append(food)
else:
    print("Stava rätt")

    