MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def isSufficient(typeCofee, resources):
    dicOfResourcesToMakeCoffee = MENU[typeCofee]["ingredients"]
    isSufficient = True
    for resource in dicOfResourcesToMakeCoffee:
        if dicOfResourcesToMakeCoffee[resource] > resources[resource]:
            difference = dicOfResourcesToMakeCoffee[resource] - resources[resource]
            gramature = "ml" if resource != "coffee" else "g"
            print(f"Insufficient {resource} to make coffee! Need {difference}{gramature} more of {resource}")
            isSufficient = False
    if isSufficient != True:
        return False
    return True

def updateResources(resourcesToMakeCoffee,resources):
  for k in resourcesToMakeCoffee:
    if k in resources:
      resources[k] -= resourcesToMakeCoffee[k]
  return resources

def coinChangeDispenser(order):
  total = 0 
  while True:
    pennies = int(input("How many pennies you giving?\n"))
    nickel = int(input("How many nickels you giving?\n"))
    dime = int(input("How many dimes you giving?\n"))
    quarter = int(input("How many quarters you giving?\n"))
    total = pennies *0.01 + nickel *0.05 + dime *0.1 + quarter * 0.25
    if total >= MENU[order]["cost"]:
      return total - MENU[order]["cost"]
    else:
      print(f'Insufficient funds total was ${round(total,2)} while ${MENU[order]["cost"]} needed to buy a {order}')




def orderCheck(order,resources,profit):
  canIMakeCoffee = None
  if order.lower() == "report":
    print(f'Water: {resources["water"]}ml \nMilk: {resources["milk"]}ml\nCoffee: {resources["coffee"]}g\nMoney: ${profit}')
    return
  elif order.lower() == "espresso" or order.lower() == "latte" or order.lower() == "cappuccino":
    canIMakeCoffee = isSufficient(order,resources)
    return canIMakeCoffee

resources1 = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

gameOn = True
profit = 0
while gameOn:
  order = input("What would you like to order?(espresso/latte/cappuccino)\n").lower()
  if order == "off":
    break
  makeCoffee = orderCheck(order,resources,profit)
  if makeCoffee:
    print("plz insert coins\n")
    change = coinChangeDispenser(order)
    print(f"Here is your Change ${round(change,2)}\n")
    updateResources(MENU[order]["ingredients"],resources)
    print(f"Here is your {order} ☕ Enjoy!\n")
    profit += MENU[order]["cost"]
  else:
    decision = input("Type Y to refill coffee machine\n").lower()
    if decision == "y":
      resources = resources1
