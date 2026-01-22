
while True:
    number_1 = int(input("your number:"))
    Fun_1 = (number_1 / 3)
    
    Fun_2 = (number_1 / 5)

    if Fun_1.is_integer() and Fun_2.is_integer():
        print("Fizzbuzz")
    elif Fun_1.is_integer():
        print("fizz")
    elif Fun_2.is_integer():
        print("buzz")
    else: 
        print(number_1)
