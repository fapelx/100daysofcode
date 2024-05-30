from turtle import Turtle

tim = Turtle()

def triangle(turtleboy):
  for i in range(3):
    turtleboy.forward(100)
    turtleboy.right(120)
    

def square(turtleboy):
  for i in range(4):
    turtleboy.forward(100)
    turtleboy.right(90)

def pentagon(turleboy):
  for i in range(5):
    turleboy.right(72)
    turleboy.forward(100)

def hexagon(turtleboy):
  for i in range(6):
    turtleboy.forward(100)
    turtleboy.right(60)

def heptagon(turtleboy):
  for i in range(7):
    turtleboy.forward(100)
    turtleboy.right(51 + 3/7)

def octagon(turtleboy):
  for i in range(8):
    turtleboy.forward(100)
    turtleboy.right(360/8)

def nonagon(turtleboy):
  for i in range(9):
    turtleboy.forward(100)
    turtleboy.right(360/9)

def decagon(turtleboy):
  for i in range(10):
    turtleboy.forward(100)
    turtleboy.right(360/10)    
triangle(tim)
square(tim)
pentagon(tim)
hexagon(tim)
heptagon(tim)
octagon(tim)
nonagon(tim)
decagon(tim)
input()