a = input("entrer un nombre: ")
while a.isdigit() == False :
    a = input("Vous devez entrer un nombre: ")

a = int(a)
s = 0

for i in range(1,a):
    if a%i==0:
        s = s+i

if s==a:
    print(a," est parfait")
else :
    print(a," n'est pas parfait")
