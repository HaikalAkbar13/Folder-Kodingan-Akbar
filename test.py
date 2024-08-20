from main import  encrypt, decrypt

text = 'Haikal'
costum = 'python'

encrypted = encrypt(text, costum)
print(encrypted)
print(decrypt(encrypted, costum))
