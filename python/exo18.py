x = input("entrer la valeurde x: ")
while x.isdigit() == False:
    x = input("vous devez entrer un entier: ")
n = input("entrer la valeurde n: ")
while n.isdigit() == False:
    n = input("vous devez entrer un entier: ")

x = int(x)
n = int(n)

a, b = x, n

while a != b:
    if a > b:
        a = a-b
    else:
        b = b-a
print("Le PPCM de ", x, " et ", n, " est ", (x*n)//a)
