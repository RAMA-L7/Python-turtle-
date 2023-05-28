from turtle import *
import turtle

background = turtle.Screen()
background.bgcolor("white")

tur = turtle.Turtle()
tur.shape ("turtle")
tur.speed(100)

def draw_mickymouse(turt, clr, siz, i,j):
  turt.penup()
  turt.color(clr)
  turt.fillcolor(clr)
  turt.goto(i,j)
  turt.pendown()
  turt.begin_fill()
  turt.circle(siz)
  turt.end_fill()
  
draw_mickymouse(tur, "black", 80, 0, -60)
draw_mickymouse(tur, "black", 45, 60, 60)
draw_mickymouse(tur, "black", 45, -60, 60)

draw_mickymouse(tur, "white", 40, 0, -60)
draw_mickymouse(tur, "white", 20, 60, 60)
draw_mickymouse(tur, "white", 20, -60, 60)
turtle.done()