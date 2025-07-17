import turtle
from turtle import Turtle, Screen
import random
turtle.colormode(255)
timmy = Turtle()

def random_color():
    r=random.randint(0,255)
    g= random.randint(0,255)
    b=random.randint(0,255)
    random_color = (r,g,b)
    return random_color
timmy.pensize(20)
timmy.shape("turtle")
timmy.speed("fastest")

random_turning = [0,90,180,270]
for i in range(30):
    timmy.color(random_color())
    timmy.forward(30)
    timmy.setheading(random.choice(random_turning))









screen = Screen()
screen.exitonclick()

