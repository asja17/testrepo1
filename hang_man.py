
# start
x=0
k=0
min_lista = []

password = input("write a word: ")
length = len(password)


while x < length:
    x=(x+1)
    min_lista.append("-")
print (f"there are {x} letters in the word: {password}")



while k < (length):
    
    letter = input ("guess a letter in the word: ")
    z=0


    for a in password:
        
        if letter[0] == password[z]:
            del min_lista[z]
            min_lista.insert(z, password[z])
            z=z+1
        else:
            z=z+1
        
    k=k+1
    
    print(min_lista)

  

    