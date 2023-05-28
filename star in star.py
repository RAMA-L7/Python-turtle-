from turtle import*
speed(9)
A = Turtle()
color('red')
begin_fill()
def star(turtle, size):
        if size<=10:
             return
        else:
           for i in range(5):
               forward(size)
               star(turtle, size/3)
               left(216)
                         
star(A, 200)
end_fill()
done()