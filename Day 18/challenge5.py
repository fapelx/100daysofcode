from turtle import Turtle,Screen
import random


screen = Screen()
screen.colormode(255)

tim = Turtle()
tim.speed("fastest")
def changecolor():
  r= random.randint(0,255)
  g= random.randint(0,255)
  b= random.randint(0,255)
  tple = (r,g,b)
  return tple

def makecircle():
  tim.circle(50)

for i in range(300):
  tim.color(changecolor())
  makecircle()
  tim.left(5)

screen.mainloop()