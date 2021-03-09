##Program to guess the number
import random
number = random.randint(0,10)
guessNum = int(input("I'm thinking of a number. Can you guess it "))

while True:

 if (guessNum == number):
     print("Your guessed it!!I was thinking about",number )
     break
 else:
    guessNum = int(input("Nope.Try Again!!"))
