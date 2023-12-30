
# start
x=0
z=0
k=0

password = input("write a word: ")
length = len(password)


while x < length:
    x=(x+1)
print (f"there are {x} letters in the word: {password}")



while k < (length):
    
    letter = input ("guess a letter in the word: ")
    z=0
    for a in password:
        if letter[0] == password[z]:
            print(letter)
        else:
            print("*")
        z=z+1
    k=k+1

  

    