from turtle import*
bgcolor('black')
speed(30)
col=('yellow','red','pink','blue','white','gray','green','orange')
goto(100,100)
for i in range(50):
    
    pencolor(col[i%6])
    circle(190-i/5,90)
    lt(90)
    circle(190-i/8,90)
    lt(60)
    
done()