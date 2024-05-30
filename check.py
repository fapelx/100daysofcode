MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    }
}
inputUser = "espresso"
for k,v in MENU[inputUser]["ingredients"].items():
  print(k,v)
  