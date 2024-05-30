from turtle import Turtle,Screen


def draw_circle(turtle):
  count = 0

  while count < 4:
    turtle.forward(100)
    turtle.right(90)
    count += 1

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("red")
draw_circle(timmy_the_turtle)
input()
