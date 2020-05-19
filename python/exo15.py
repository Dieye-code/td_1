a = input("entrer un nombre: ")
while a.isdigit() == False:
    a = input("vous devez entrer un nombre")
a = int(a)
s = 0
for i in range(a+1):
    s +=i
print("La somme des nombre de 1 a ",a," est ",s)

print("La moyenne des nmbres entre 1 et  ", a, " est ", s/a)
