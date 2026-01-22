while True:
    start = int(input("First number: "))
    stop = int(input("Second number: "))

    for i in range(start, stop + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")   
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)