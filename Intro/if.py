print("how old are ya?")

age = input()
age = int(age)

if age < 18:
    print ("stupid child")
elif age >= 18 and age <50:
    print("u're a grown up")
elif age >= 50: 
    print("Bloody hell, u're old")