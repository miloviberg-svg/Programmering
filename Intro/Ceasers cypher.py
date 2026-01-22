alphabet = "abcdefghijklmnopqrstuvwxyzåäö"

def caesar_cipher(text, shift):
    result = ""

    for char in text:
        if char.isupper():
            pos = alphabet.index(char.lower())
            shifted_pos = pos + shift % len(alphabet)
            result += alphabet[shifted_pos].upper()
        elif char.islower():
            result += alphabet[(alphabet.index(char) + shift) % len(alphabet)]
        else:
            result += char  

    return result

while True:
    text = input("Skriv en mening som ska krypteras: ")
    shift = int(input("Hur många steg ska den krypteras? : "))

    encrypted_text = caesar_cipher(text, shift)

    print("Krypterad text:")
    print(encrypted_text)
