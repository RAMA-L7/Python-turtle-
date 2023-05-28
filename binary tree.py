from turtle import*
lt(90)
speed(0)
bgcolor('black')
color('white')

def tree(i):
    if i<20:
        return
    else:
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