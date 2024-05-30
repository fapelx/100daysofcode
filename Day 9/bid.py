from art import logo

def highest_bid(bid_record):
  highest = 0
  winner = ""
  for k,v in bid_record.items():
    if v > highest:
      highest = v
      winner = k
  print(f"Winner is {winner} with a ${highest} bid")


print(logo)
dic = {}
while(True):
  name = input("Welcome to bid auctions plz give me ur name\n")
  price = input("What's your bid?\n")
  dic[name]=int(price)
  anyother = input("Are there any other players that want to bid?y/n \n").lower()
  if anyother == "n":
    highest_bid(dic)
    break
  
