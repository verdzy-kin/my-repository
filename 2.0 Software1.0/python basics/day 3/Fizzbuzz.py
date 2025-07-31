# #FIZZBUZZ GAME 
# while True:
#     userInput = input("Enter 'Continue' to go ahead with the game and 'Exit' to stop: ").strip().lower()
#     if userInput == "Exit":
#         print("The end")
#         break
#     elif userInput == "continue":
#         number = int(input("Enter number: "))
#         if number%3 == 0 and number%5 == 0:
#             print("FIZZBUZZ")
#         elif number % 3 == 0:
#             print("FIZZ")
#         elif number % 5 == 0:
#             print("BUZZ")
#         else:
#             print(f"{number}")
#     else:
#         print("UNRECOGNISED!!!")


# #SWAPPING EXERCISE

# a = input("Enter a: ")
# b = input("Enter b: ")
# c = a

# print(f"a = {b} and b = {c}")



#GUESSING GAME
import random
range=int(input("Enter range: "))
Randominteger = random.randint(0,range)
guess = 0
maxGuess = 3
while guess < maxGuess:
    global answer
    answer=int(input("Guess the number I generated: "))
    guess += 1  
    if answer > Randominteger:
        print("you are below target")
    elif answer < Randominteger:
        print("you are above target")
    elif answer == Randominteger:
        print("you got it right")
        break
    else:
        print("invalid!!!")
if guess == maxGuess and answer != Randominteger:
    print(f"computer wins, the value was {Randominteger}")