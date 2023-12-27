
# start
x=0
fråga = input("write a word: ")

word = len(fråga)

while x < word:
    x = (x+1)
print (f"there are {x} letters in the word")


# lifes
chans= ["*","*","*"]
print (f"this is your lifes {chans}")

guess = input ("guess a letter in the word: ")

if guess == word:
    print(" * * ") 
else:
    print(" * * *  Good job")