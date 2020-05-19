import math

print("Equation du second degrés")
a = input("A : ")
while a.isdigit() == False:
    a = input("vous devez entré un entier : ")
b = input("B : ")
while b.isdigit() == False:
    b = input("vous devez entré un entier : ")
c = input("C : ")
while c.isdigit() == False:
    c = input("vous devez entré un entier : ")

a = int(a)
b = int(b)
c = int(c)

d = b**2 -4*a*c

if d<0:
    print("La solution n'existe pas dans R")
elif d==0:
    print("X={",-b/2*a,"}")
else :
    x1 = round((-b-math.sqrt(d))/2*a)
    x2 = round((-b+math.sqrt(d))/2*a)
    print("X{", x1 , ",", x2 ,"}")
