a = input("Entrer le nombre à deviner")
while a.isdigit() == False:
    a = input("vous devez saisir un nombre")
a = int(a)

b = 0
d = 0

while b == 0:
    c = input("Entrer un nombre: ")
    while c.isdigit() == False:
        c = input("vous devez saisir un nombre")
    c = int(c)
    d = d+1
    if c > a:
        print("trop grand")
    elif c < a:
        print("Trop petit")
    else:
        print("Bravo vous avez trouvé le nombre ", a," a ",d," tentatives")
        b = 1
