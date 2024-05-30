from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
my_coffee_maker = CoffeeMaker()
my_money_machine = MoneyMachine()
my_menu = Menu()
coffee = True
 
while  coffee:
  order_name = input("What do you want to order? ")
  if order_name == "report":
    my_coffee_maker.report()
    my_money_machine.report()
  elif order_name == "off":
    coffee = False
  else:
    drink = my_menu.find_drink(order_name)
    if my_coffee_maker.is_resource_sufficient(drink):
      if my_money_machine.make_payment(drink.cost):
        my_coffee_maker.make_coffee(drink)