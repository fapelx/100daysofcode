#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
import random
from logo import logo
def correctInputLevel(levelInput):
  incorrect_input = True
  while incorrect_input:
    if levelInput == "easy":
      lives = 10
      return lives
    elif level == "hard":
      lives = 5
      return lives
    else:
      print("Incorrect input set a difficulty level in order to choose easy type easy hard type hard")

def gameLogic(guess,number):
  commentary = ""
  if guess > number:
    commentary = "Too high\n"
    return commentary
  elif guess < number:
    commentary = "Too low\n"
    return commentary
  else:
    commentary = "You won!\n"
    return commentary
  
print(logo)
print("Welcome to number guessing game!\n")
lives = 0
level = input("What level difficulty you want to set hard or easy?\n").lower()
lives = correctInputLevel(level)
number = random.randint(1,101)
gameOn = True
while gameOn:
  guess = int(input("Make a guess!Number is between 1-100: \n"))
  result = gameLogic(guess,number)
  if result == "You won!\n":
    print(f"You won the number was {number}")
    break
  else:
    print(result + "Guess again!\n")
    lives -= 1
    print(f"You have {lives} attempts left!\n")
  if lives == 0:
    print("You run out of attempts!Game over!\n")
    print(f"The number was {number}")
    break



