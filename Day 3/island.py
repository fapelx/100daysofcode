print("Welcome to Treasure Island.Your mission is to find the treasure.\n")
left_right = input("Do you want to go left or right?Write R or L\n").upper()

if left_right == "L":
  print("congrats you survived round 1\n")
  swim_wait = input("What to do now swim or wait?Write S or W\n").upper()
  if swim_wait == "W":
    print("congrats you survived round 2\n")
    door = input("Which door you are choosing red,blue or yellow?Write R or B or Y\n").upper()
    if door == "Y":
      print("Congrats you won the game!\n")
    else:
      print("You lost\n")  
  else:
    print("You lost\n")

else:
  print("You lost\n")