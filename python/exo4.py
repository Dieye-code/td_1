x = input("Entrer x: ")
while x.isdigit() == False:
    x = input("Vous devez entrer un entier: ");
n = input("Entrer n: ")
while n.isdigit() == False:
    n = input("Vous devez entrer un entier: ")

x = int(x)
n = int(n)

s=1

for i in range(n):
    s = s*x

print (x,"^",n,"=",s);
