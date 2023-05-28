from turtle import*
hideturtle()
speed(90)
def star(turtle, size):
        color('red')
        begin_fill()
        if size<=10:
             return
        else:
           for i in range(5):
               forward(size)
               star(turtle, size/3)
               left(216)
               
               
for angle in range(0,90):
    up()
    goto(0,0)
    seth(angle*4)
    down()
    pensize(0)
    color("#00ff00")
    fd(100)
    pensize(1)
    color('#00ff00')
    circle(100,50)
    pensize(2)
    color('#00ff00')
    circle(-450,30)
    pensize(1)
    circle(90,50)
    color('#00ff00')
    begin_fill()
    star(0,15)
    end_fill()
    

    
done()   