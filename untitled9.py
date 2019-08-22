#vignercipher

key = input("enter the key ")
key.lower()
plaintext = input("enter the plain text ")
plaintext=plaintext.lower()
a='abcdefghijklmnopqrstuvwxyz'
ciphertext=''
for i in range(len(plaintext)):
    l=(ord(plaintext[i])%97+ord(key[i])%97)%26
    l=a[l]
    ciphertext=ciphertext+l
print(ciphertext)


ciphertext1='dpnxwxjzwwjqvbblzbdqu'
decryp=''
for i in range(len(ciphertext1)):
    l=(ord(ciphertext1[i])%97-ord(key[i])%97)%26
    l=a[l]
    decryp=decryp+l
print(decryp)
