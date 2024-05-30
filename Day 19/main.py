from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500,height=400)
user_bet = screen.textinput(title = "Make your bet",prompt="Which turtle win win the race?Enter a color: ")

israceon = False

yaxis = -100
colors = ["red","orange","yellow","purple","green","black"]
def create_turtle():
  global yaxis 
  global colors
  colort = random.choice(colors) 
  turtle = Turtle(shape="turtle")
  turtle.color(colort)
  turtle.penup()
  turtle.goto(x=-230,y=yaxis)
  yaxis += 40
  colors.remove(colort)
  return turtle

turtles = []

for i in range(6):
  turtles.append(create_turtle())


if user_bet:
  israceon = True

while israceon:
  
  for turtle in turtles:
    if turtle.xcor()> 230:
      israceon = False
      winningcolor = turtle.pencolor()
      if winningcolor == user_bet:
        print(f"You won!The winning color was {winningcolor}")
      else:
        print(f"You lost!The winning color was {winningcolor}")

    rand_distance = random.randint(0,10)
    turtle.forward(rand_distance)
screen.exitonclick()