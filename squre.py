from turtle import*
speed(9)
colours=('green','blue','red','black','pink')
for i in range(100):
    fd(i*10)
    rt(90)
    color(colours [i%5])
          
done()