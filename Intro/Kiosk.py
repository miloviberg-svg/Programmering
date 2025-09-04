print("Welcome, what could i get ya? We have ice cream, hotdogs, soda and candy")
item = input()

if item == "ice cream":
    print("how many ice creams would you like?")
    x = input()
    x = int(x)
    print("that will be", x * 20, "kr")
elif item == "hotdogs":
    print("how many hotdogs would you like?")
    x = input()
    x = int(x)
    print("that will be", x * 15, "kr")
elif item == "soda":
    print("how many sodas would you like?")
    x = input()
    x = int(x)
    print("that will be", x * 15, "kr")
elif item == "candy":
    print("how many candies would you like?")
    x = input()
    x = int(x)
    print("that will be", x * 10, "kr")

print("thank you for your purchase, have a nice day")