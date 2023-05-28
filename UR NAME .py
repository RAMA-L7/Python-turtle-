import pyfiglet
s1 = input("what is ur name?")
s2 = "" 
for i in s1:
    s2 = s2 + i + '\n'
print(s2)
#s2= input("what is ur name?")
name=pyfiglet.figlet_format(s2
,font='3-d')
print(name)
name=pyfiglet.figlet_format(s2,font='banner')

print(name)

