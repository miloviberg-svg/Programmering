Lista = ["potatis"]
answer_5 = input("Vill du se listan? ")
if answer_5 == "ja" or "Ja":
    print(Lista)
    
answer_1 = input("Vill du lägga till något i listan? " )

if answer_1 == "ja" or answer_1 == "Ja":
    var_1 = input("Vad vill du lägga till ")
    Lista.append(var_1)
    while True:
        answer_2 = input("Vill du lägga till något mer? " )
        if answer_2 == "ja" or answer_2 == "Ja":
            var_2 = input("vad vill du lägga till ")
            Lista.append(var_2)
        else:
            break
    answer_3 = input("vill du ta bort något från listan? ")
    if answer_3 == "ja" or answer_3 == "Ja":
        var_3 = input("vad vill du ta bort? ")
        Lista.remove(var_3)
        while True:
            answer_4 = input("vill du ta bort något mer? ")
            if answer_4 == "ja" or answer_4 == "Ja":
                var_4 = input("vad vill du ta bort? ")
                Lista.remove(var_4)
            else:
                break
            
    answer_5 = input("Vill du se listan? ")
    if answer_5 == "ja" or answer_5 == "Ja":
        print(Lista)