def subtraction(x,y):
        return x - y
def addition(x,y):
        return x + y
def division(x,y):
        return x / y
def multiplication(x,y):
        return x * y

while True:
    number_1= int(input("First number:"))
    number_2 = int(input("second number:"))

    print("-, +, / eller *?")
    fun = input()
    if number_2 == 0 and fun == "/":
          print("Fuck you")
    elif fun == "-":
        result = subtraction(number_1,number_2)
        print(result)
    elif fun == "+":
        result = addition(number_1,number_2)
        print(result)
    elif fun == "/":
        result = division(number_1,number_2)
        print(result)
    elif fun == "*":
        result = multiplication(number_1,number_2)
        print(result)
    else:
        print("invalid operator")