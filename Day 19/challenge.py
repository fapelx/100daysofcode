from turtle import Turtle,Screen

tim = Turtle()
screen = Screen()

def moveforward():
  tim.forward(10)

def left():
  tim.left(10)
  tim.forward(10)

def right():
  tim.right(10)
  tim.forward(10)

def backwards():
  tim.backward(10)

def clear():
  tim.penup()
  tim.goto(0,0)
  tim.clear()
  tim.setheading(90)
  tim.pendown()
  

screen.listen()
tim.setheading(90)
screen.onkey(key = "w", fun = moveforward)
screen.onkey(key = "a", fun = left)
screen.onkey(key = "d", fun = right)
screen.onkey(key = "s", fun = backwards)
screen.onkey(key = "c", fun = clear)
screen.exitonclick()