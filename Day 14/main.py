from art import logo,vs
from game_data import data
import random
#name , follower_count , description , country 

def chooseData():
  choice = random.randint(0,len(data)-1)
  return data[choice]


def isPlayerRight(playerChoice,computerChoice,c):
  moreFollowers = ""
  if playerChoice["follower_count"] > computerChoice["follower_count"]:
    moreFollowers = "a"
  elif playerChoice["follower_count"] < computerChoice["follower_count"]:
    moreFollowers = "b"
  else:
    moreFollowers = ""
  if moreFollowers == c or moreFollowers is None:
    print(f'Your right!\n')
    print(f'{playerChoice["follower_count"]} vs {computerChoice["follower_count"]}')
    return True
  else:
    print(f'{playerChoice["follower_count"]} vs {computerChoice["follower_count"]}')
    return False


def compare(playerChoice,computerChoice):
  print(f'Compare A:{playerChoice["name"]}, {playerChoice["description"]}, {playerChoice["country"]}\n')
  print(vs)
  print(f'Against B:{computerChoice["name"]}, {computerChoice["description"]}, {computerChoice["country"]}\n')
  decision = input("Who has more followers A or B?").lower()
  guess = isPlayerRight(playerChoice,computerChoice,decision)
  if guess:
    return True
  else:
    return False


def youLose(a):
  print(logo)
  print(f"Sorry that's wrong your final score {a}")

gameOn = True
score = 0

playerChoice = chooseData()

while gameOn:
  print(logo)
  computerChoice = chooseData()
  while computerChoice["name"] == playerChoice["name"]:
    computerChoice = chooseData()
  guess = compare(playerChoice,computerChoice)
  if guess:
    score += 1
    print(f"Current score {score}\n")
  else:
    youLose(score)
    break
  continue_input = input("Do you wish to continue y/n?\n").lower()
  if continue_input == "n":
    break
  playerChoice = computerChoice


