from turtle import Turtle
import random
tim = Turtle()

turn = ["left","right"]
directions = [0,90,180,270]
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]


tim.pensize(15)
tim.speed("fastest")

for i in range(50):
  tim.color(random.choice(colours))
  how_much = random.choice(directions)
  tim.setheading(how_much)
  tim.forward(30)

