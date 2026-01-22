

def addition(x, y):
    return x + y

def subtraction(x, y):
    return x - y

def division(x, y):
    return x / y

def multiplication(x, y):
    return x * y

while True:
    number_1 = int(input("Enter first number: "))
    number_2 = int(input("Enter second number: "))

    print("Choose operation: -, +, /, * (or type q to quit)")
    fun = input()

    if fun == "-":
        print(subtraction(number_1, number_2))
    elif fun == "+":
        print(addition(number_1, number_2))
    elif fun == "/":
        print(division(number_1, number_2))
    elif fun == "*":
        print(multiplication(number_1, number_2))
    elif fun.lower() == "q":
        print("Exiting...")
        break
    else:
        print("Invalid operator, try again!")