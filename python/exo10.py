a = input("entrer la valeur de a: ")
while a.isdigit() == False:
    a = input("vous devez entré un entier : ")

b = input("entrer la valeur de b: ")
while b.isdigit() == False:
    b = input("vous devez entré un entier : ")

c = input("entrer la valeur de c: ")
while c.isdigit() == False:
    c = input("vous devez entré un entier : ")

a = int(a)
b = int(b)
c = int(c)


def echange(x, y):
    if x > y:
        c = x
        x = y
        y = c
    return x,y

a,b = echange(a,b)
a,c = echange(a,c)
b,c = echange(b,c)

print(a," - ",b," - ",c)

