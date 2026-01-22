print("Hej, * = gånger,- = minus, + = plus, / = delat, ** upphöjt")


x = input()
x = int(x)

z = input()

y = input()
y = int(y)

if z == "*":
    print(x * y)
elif z == "-":
    print(x-y)
elif z == "+":
    print(x + y)
elif z == "/":
    print(x / y)
elif z == "**":
    print(x ** y)
