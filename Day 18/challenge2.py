from turtle import Turtle

tim = Turtle()

for i in range(10):
  tim.forward(10)
  tim.penup()
  tim.forward(10)
  tim.pendown()

input()