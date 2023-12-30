
# start
x=0
z=0
k=0

password = input("write a word: ")
length = len(password)

while x < length:
    x=(x+1)
print (f"there are {x} letters in the word: {password}")



while k <= 4:
    Letter = input ("guess a letter in the word: ")
    if Letter[0] == password[z]:
        z=z+1
        print("correct")
    else:
        print("wrong")
    k=k+1

  

    