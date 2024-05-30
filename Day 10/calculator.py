
#calculator
from art import logo
print(logo)

#add
def add(n1,n2):
  return n1 + n2
#subs
def subs(n1,n2):
  return n1 - n2
#multi
def multi(n1,n2):
  return n1*n2
#div
def div(n1,n2):
  return n1/n2

operations = {
  "+":add,
  "-":subs,
  "*":multi,
  "/":div
}
num3 = None
while(True):
  if (num3 is None):
    num1 = int(input("What's your first number?\n"))
    decision = input("What operation you wish to do to choose from these(+,-,*,/)?\n")
  else:
    print(num3)
    decision = input("What operation you wish to do to choose from these(+,-,*,/)?\n")
    num1 = int(input("What's next number?\n"))
  
  if num3 is None:
    num2 = int(input("What's your second number?\n"))

  for symbol in operations:
    if decision == symbol:
      if num3 is None:
        print(operations[decision](num1,num2))
        num3 = operations[decision](num1,num2)
      else:
        print(operations[decision](num3,num1))
        num3 = operations[decision](num3,num1)

  end = input("Do you wish to continue? y/n?").lower()
  if end == "n":
    print("Thanks for using this app")
    break