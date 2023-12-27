
# start
x=0
password = input("write a word: ")

length = len(password)

while x < length:
    x = (x+1)
print (f"there are {x} letters in the word: {password}")
print ("You will get 3 chances to guess this word")


Letter = input ("guess a letter in the word: ")
print("you guessed:"+ Letter[0])

if Letter[0] == password[0] : print("Correct")



