odds=[2,4,6,8,10,12,14]
evens=[1,3,5,7,9,11,13,15]
prime=[2,3,5,7,11,13]
num = odds + evens + prime
print(type(num))
print(num)
num=set(num)
print(type(num))
print(num)
print(len(num))
num.add(0)
print(num)
print(len(num))
num.discard(15)
print(num)

