from turtle import  Turtle
import random

def random_walk(turtle, turns, distance=60):
    turtle.width(6)
    for x in range(turns):
        turtle.rt(random.randint(0,360))
        turtle.fd(distance)
random_walk(Turtle(),300)