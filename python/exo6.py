import math

print("Etrer les coordonnées du point A")
x1 = input("x: ")
while x1.isdigit() == False:
    x1 = input("Vous devez entrer un entier: ")
y1 = input("y: ")
while y1.isdigit() == False:
    y1 = input("Vous devez entrer un entier: ")

print("Etrer les coordonnées du point B")
x2 = input("x: ")
while x2.isdigit() == False:
    x2 = input("Vous devez entrer un entier: ")
y2= input("y: ")
while y2.isdigit() == False:
    y2 = input("Vous devez entrer un entier: ")


x1 = int(x1)
y1 = int(y1)
x2 = int(x2)
y2 = int(y2)

p = math.sqrt(((x1-x2)**2)+((y1-y2)**2))

print("La distance entre A(",x1,",",y1,") et B(",x2,",",y2,") est ",p)
