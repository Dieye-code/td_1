s = 0

for i in range(5):
    x = input("un nombre: ")
    while x.isdigit() == False:
        x = input("Vous devez entrer un entier: ")
    x = int(x);
    s = s+x

print("la somme des nombre de 1 a 5 est ", s)
