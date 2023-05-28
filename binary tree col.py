from turtle import*
import colorsys
lt(90)
speed(0)
tracer(30)
bgcolor('black')
color('white')
h=1
n=200
h+=1/n
def tree(i):
    if i<10:
       
        
        return
    else:
        c=colorsys.rgb_to_yiq(1.83266,0.32633,0.85584)
        pencolor(c)
        pensize(3*i/30)  
        fd(i)
        lt(30)
        tree(3*i/4)
        rt(60)
        tree(3*i/4)
        #rt(30)
       # tree(3*i/4)
        lt(30)
        backward(i)
        
        
tree(250)
done()                        