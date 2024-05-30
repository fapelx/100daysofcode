import random 
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

ask_user = input("rock,paper,scissors choose!write r,p,s").lower()
if ask_user == "r":
  ask_user = rock
elif ask_user == "p":
  ask_user = paper
elif ask_user == "s":
  ask_user = scissors
print("Your move:\n" + ask_user)

computer_move = random.randint(0,2)

if computer_move == 0:
  computer_move = rock
elif computer_move == 1:
  computer_move = paper
elif computer_move == 2:
  computer_move = scissors

print("Computers move:\n" + computer_move)

if ask_user == computer_move:
  print("tie!")
elif ask_user == rock and computer_move == scissors:
  print("You won!")
elif ask_user == rock and computer_move == paper:
  print("You lost!")
elif ask_user == paper and computer_move == rock:
  print("You won!")
elif ask_user == paper and computer_move == scissors:
  print("You lost!")
elif ask_user == scissors and computer_move == rock:
  print("You lost!")
elif ask_user == scissors and computer_move == paper:
  print("You won!")