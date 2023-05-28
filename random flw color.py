from turtle import*
from random import randint
import colorsys
tracer(300)
x =10
y =10
h=0
n=210
    
    
bgcolor('black')
speed(0)
pensize(3)
#col=('yellow','red','pink','blue','white','gray','green','orange')

#for r in range(-500,500,100):
#        if x in r:
#            x=10+r
#            y=10+r
#            penup()
#            goto(x,y)
#            pendown()
for k in range(500):
    h+=5/n
    penup()
    goto((randint(-500,500)),(randint(-1000,1000)))
    pendown()
    pensize(k*0.01)
    for i in range(12):
        #bgcolor(col[i%8])
        #pencolor(col[i%6])
        c=colorsys.hsv_to_rgb(h,1,1)
        pencolor(c)
        circle(40-i/5,90)
        lt(90)
        circle(40-i/8,90)
        lt(60)
      
        
done()