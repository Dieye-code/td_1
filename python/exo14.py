print("Entrer la date")
j = input("J: ")
while j.isdigit() == False:
    j = "vous devez saisir un entier"

m = input("M: ")
while m.isdigit() == False:
    m = "vous devez saisir un entier"

a = input("A: ")
while a.isdigit() == False:
    a = "vous devez saisir un entier"

j = int(j)
m = int(m)
a = int(a)

if a %400 == 0 or a%4 == 0 and a%100 != 0:
    print( a, " est bisextile")
else:
    print(a, " n'est pas bisextile")
