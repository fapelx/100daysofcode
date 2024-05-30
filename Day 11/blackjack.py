############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   https://appbrewery.github.io/python-day11-demo/
import random

def dealer_card_give():
  choice = random.randint(0,len(cards)-1)
  card = logos[choice]
  points = cards[choice]
  return points,card

def whoWon(playerPoints,compPoints):
      commentary = ""
      if compPoints > 21 and playerPoints > 21:
         commentary = "You both went over a draw!"
         return commentary 
      elif compPoints > 21:
         commentary = "You won computer went over!"
         return commentary
      elif playerPoints > 21:
         commentary = "You lost you went over!"
         return commentary
      elif playerPoints > compPoints:
         commentary = f"You won by a {playerPoints-compPoints} points!"
         return commentary
      elif compPoints > playerPoints:
         commentary = f"You lost by a {compPoints-playerPoints} points!"
         return commentary
      else:
         commentary = f"A draw you both have a {playerPoints} points!"
         return commentary

def changeAce(totalPoints,deck):
   if totalPoints > 21 and any(card.lower() == 'ace' for card in deck if isinstance(card, str)):
      totalPoints = totalPoints - 10
      return totalPoints
   else:
      return totalPoints
            
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

logos = {
  0:'Ace',
  1:2,
  2:3,
  3:4,
  4:5,
  5:6,
  6:7,
  7:8,
  8:9,
  9:10,
  10:"Joker",
  11:"Queen",
  12:"King"
}

while(True):
  card1_player,figure1_player=dealer_card_give()

  card1_comp,figure1_comp = dealer_card_give() 

  card2_player,figure2_player = dealer_card_give()

  player_total_points = card1_player + card2_player

  player_deck = [figure1_player,figure2_player]

  print(f"Your deck is {player_deck} you got a total of {player_total_points} points.\n")

  print(f"Computer has chosen a {figure1_comp} it got a total of {card1_comp} points.\n")

  card2_comp,figure2_comp = dealer_card_give()

  comp_total_points = card1_comp + card2_comp

  comp_deck = [figure1_comp,figure2_comp]

  decision = input("Do you wish to get a 1 more card y/n?\n").lower()

  if decision == "y":

    if comp_total_points < 17:

      card3_comp,figure3_comp = dealer_card_give()

      comp_total_points += card3_comp

      comp_deck.append(figure3_comp)

      comp_total_points = changeAce(comp_total_points,comp_deck)    

    card3_player,figure3_player = dealer_card_give()

    player_total_points += card3_player

    player_deck.append(figure3_player)

    player_total_points = changeAce(player_total_points,player_deck)

    print(f"Your deck is {player_deck}")

    print(f"Computer deck is {comp_deck}")

    print(whoWon(player_total_points,comp_total_points))
  else:
    print(f"Your deck is {player_deck}")

    print(f"Computer deck is {comp_deck}")

    print(whoWon(player_total_points,comp_total_points))

  continueGame = input("Do you want to play more?y/n \n").lower()

  if continueGame == "n":
     
     break