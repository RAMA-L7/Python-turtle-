speed=int(input("enter the speed of wind in knotes\n"))

if speed<10:
    print("calm")
elif speed<30:
    print("light air")
elif 30<=speed<=50:
    print("Breeze")
elif 51<=speed<=70:
    print("Gales")  
else:
    print("Hurricane")    