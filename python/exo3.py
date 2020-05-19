r1 = input("Entrer la resistance R1 : ");
while r1.isdigit== False:
    r1 = input("Vous devez entrer un entier : ");

r2 = input("Entrer la resistance R2 : ")
while r2.isdigit == False:
    r2 = input("Vous devez entrer un entier : ")

r3 = input("Entrer la resistance R3 : ")
while r3.isdigit == False:
    r3 = input("Vous devez entrer un entier : ")

r1 = int(r1)
r2 = int(r2)
r3 = int(r3)

choix = input("Quelle type de resistance voulez-vous calculé\n1********en serie\n2******en parallele");


if choix == "1":
    rs = r1+r2+r3
    print("La resistance en serie est ",rs)
elif choix == "2":
    rp = (r1*r2*r3)//(r1*r2 + r1*r3 + r2*r3)
    print("La resistance en parallele est ", rp)
else:
    print("Votre choix n'existe pas")

