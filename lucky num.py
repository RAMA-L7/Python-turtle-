a=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
for i in a:
    if i%2!=0:
        pass
    else:
        a.remove(i)
for i in range(1,len(a)-3):
    if i%3!=0:
        pass
    else:
        a.remove(a[i])
b=int(input())        
if b in a:
    print("lucky")
else:
     print("not")