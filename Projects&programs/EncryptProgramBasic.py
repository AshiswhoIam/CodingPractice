import random
import string

#can use string.whitespace
chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()

random.shuffle(key)

#print(f"chars: {chars}")
#print(f"key  : {key}")

#Encryption here
user_msg= input("Enter something that you want encrypted: ")
cipher_msg = " "

for letter in user_msg:
    index = chars.index(letter)
    cipher_msg += key[index]

print(f"\nOriginal message  : {user_msg}")
print(f"Encrypted message : {cipher_msg}")
print()
#Decryption here
cipher_msg= input("Enter something that you want decrypted: ")
user_msg = " "

for letter in cipher_msg:
    index = key.index(letter)
    user_msg += chars[index]


print(f"Original message  : {cipher_msg}")
print(f"Encrypted message : {user_msg}")