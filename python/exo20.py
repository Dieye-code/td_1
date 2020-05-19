g = 0
p = 0

for i in range(10):
    n = input("entrer le nombre a la position ")
    while n.isdigit() == False:
        n = input("vous devez saisir un nombre: ")
    n = int(n)
    if n>=g:
        g = n
        p = i+1
print("le nombre le plus grand est ",g," sa position est ",p)