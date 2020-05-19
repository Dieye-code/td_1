import array as ar
n = 10
tab = ar.array('i', [])
for i in range(n):
    print("entrer l'element à l'indice ", i+1)
    x = input()
    while x.isdigit == False or int(x) < 1 or int(x) > 100:
        x = input("Vous devez saisir un entier compris entre 1 et 100")
    tab.append(int(x))
dc = 1
c = 1
m = 1

for i in range(n-1):
   if tab[i] < tab[i+1]:
       dc = 0
   elif tab[i] > tab[i+1]:
       c = 0


if c == 1:
    print("Les nombres sont dans l'ordre croissant")
elif dc == 1:
    print("les nombres sont dans l'ordre decroissant")
else:
    print("les nombres sont dant l'ordre quelconque")