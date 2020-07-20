import secrets
import string

random_key = ""

alphabets = "abcdefghijklmnopqrstuvwxyz"

letter_to_index = dict(zip(alphabets,range(len(alphabets))))
index_to_letter = dict(zip(range(len(alphabets)),alphabets))

encrypted_text = ""

def encryption(msg):
    encrypted = ""
    global random_key
    random_key = ''.join(secrets.choice(string.ascii_lowercase)
                                                  for i in range(len(msg)))

    print("\nYour One Time random Key is : ",random_key)
    for i in range(len(msg)):

        number = (letter_to_index[msg[i]] + letter_to_index[random_key[i]])%len(alphabets)
        if number > len(alphabets) :
            number -= len(alphabets)

        encrypted +=  index_to_letter[number]

    global encrypted_text
    encrypted_text =encrypted
    return encrypted

def decryption(cipher):
    decrypted = ""
    for i in range(len(cipher)):
        number = (letter_to_index[cipher[i]] - letter_to_index[random_key[i]])%len(alphabets)
        if number < 0 :
            number += len(alphabets)
        decrypted +=index_to_letter[number]
    return decrypted


input = input("Enter Text for Encryption :")
encrypted = encryption(input)
print("Encrypted text is :",encrypted)
print("Using this key",random_key,"your")
print("Decrypted text is :",decryption(encrypted))
print("\nNow Key is Expired")
