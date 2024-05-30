from turtle import Turtle,Screen
import random

screen = Screen()
screen.colormode(255)

tim = Turtle()

colors = [(213, 154, 96), (51, 107, 132), (202, 142, 31), (180, 77, 30), (115, 155, 171), (124, 79, 99), (122, 175, 156), (226, 198, 131), (192, 87, 108), (10, 50, 64), (55, 38, 18), (44, 168, 126), (47, 127, 123), (200, 121, 143), (168, 21, 29), (228, 92, 77), (38, 32, 35), (2, 26, 25), (78, 148, 171), (169, 23, 18), (101, 126, 159), (17, 79, 91), 
(178, 204, 185), (49, 62, 84)]
tim.penup()
tim.speed("fastest")
tim.hideturtle()
tim.forward(200)
tim.right(90)
tim.forward(200)
tim.setheading(225)
tim.forward(50)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(number_of_dots):
  if dot_count != 0:
    tim.dot(20,random.choice(colors))
    tim.forward(50)
  if dot_count % 10 == 0:
    tim.setheading(90)
    tim.forward(50)
    tim.setheading(180)
    tim.forward(500)
    tim.setheading(0)
tim.dot(20,random.choice(colors))
screen.mainloop()