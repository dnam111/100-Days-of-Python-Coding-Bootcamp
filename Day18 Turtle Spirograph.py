import turtle
from turtle import Turtle, Screen
import random
turtle.colormode(255)
timmy = Turtle()

def random_color():
    r=random.randint(0,255)
    g= random.randint(0,255)
    b=random.randint(0,255)
    color = (r,g,b)
    return color
def draw_spirograph(size_of_gap):
    for i in range(int(360/size_of_gap)):
        timmy.color(random_color())
        timmy.circle(100)
        timmy.setheading(timmy.heading()+size_of_gap)
timmy.speed("fastest")
draw_spirograph(5)
timmy.shape("turtle")
timmy.speed("fastest")








screen = Screen()
screen.exitonclick()

