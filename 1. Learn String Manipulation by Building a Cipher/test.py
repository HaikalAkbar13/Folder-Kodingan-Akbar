from main import  encrypt, decrypt

text = 'Hello Zaira!'
costum = 'python'

encrypted = encrypt(text, costum)
print(encrypted)
print(decrypt(encrypted, costum))
