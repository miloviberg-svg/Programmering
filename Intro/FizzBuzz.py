
number_1 = int(input("First number"))
number_2 = int(input("Second number"))

for i in range(number_1, number_2 + 1):
    fun_1 = (i / 3)
    fun_2 = (i / 5)
if fun_1.is_integer() and fun_2.is_integer():
    print("Fizzbuzz")
elif fun_1.is_integer():
    print("fizz")
elif fun_2.is_integer():
    print("buzz")
else: 
    print(i)