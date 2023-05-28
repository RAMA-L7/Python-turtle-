from turtle import*
from random import randint

x =10
y =10
r=300
    
    
bgcolor('black')
speed(0)
pensize(3)
col=('yellow','red','pink','blue','white','gray','green','orange')

#for r in range(-500,500,100):
#        if x in r:
#            x=10+r
#            y=10+r
#            penup()
#            goto(x,y)
#            pendown()
for k in range(120):
    penup()
    goto((randint(-500,500)),(randint(-800,800)))
    pendown()
    for i in range(12):
        #bgcolor(col[i%8])
        pencolor(col[i%6])
        circle(40-i/5,90)
        lt(90)
        circle(40-i/8,90)
        lt(60)
      
        
done()