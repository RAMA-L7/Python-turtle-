from turtle import*
bgcolor('cyan')
pensize()
speed(20)
colours=('white','blue','red')
for i in range(400):
    fd(i*4)
    rt(91)
    color(colours[i%3])
    for x in range(3):
        fd(x*4)
        rt(91)
        for a in range(2):
            fd(a*4)
            rt(91)
            for m in range(789):
                fd(m*4)
                rt(891)
done()