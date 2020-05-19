import array as ar
n = input("entrer la taille du tableau")
while n.isdigit == False or int(n)<10 or int(n) > 50:
    n = input("Vous devez saisir un entier compris entre 10 et 50")
n = int(n)
tab = ar.array('i',[])
for i in range(n):
    print("entrer l'element à l'indice ",i+1)
    x = input()
    while x.isdigit == False or int(x)<1 or int(x) > 100:
        x = input("Vous devez saisir un entier compris entre 1 et 100")
    tab.append(int(x))
db = 0
fn = 0
l = 0

for i in range(n-1):
    k = i
    while i+1 < n and tab[i] < tab[i+1]:
        i = i+1
    if (i+1)-k>l:
        db = k
        fn = i+1
        l = i+1-k
print("La sequence la plus longue est ")
for i in range(n):
    if db <= i < fn:
        print(tab[i])
print("Elle commence a la position ",db+1," et sa longeure est ",l)
