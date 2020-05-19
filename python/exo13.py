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
if j<0 and j>31 or m<1 and m>12 or a<1 and a>2020:
    print(j,"/",m,"/",a," n'est pas valide")
elif m % 2 != 0 and m <= 7 or m % 2 == 0 and m > 7:
    print(j, "/", m, "/", a, " est valide")
elif m!=2:
    if j>30:
        print(j, "/", m, "/", a, " n'est pas valide")
    else:
        print(j, "/", m, "/", a, " est valide")
else:
    if a%400==0 or a%4==0 and a%100!=0:
        if j>29:
            print(j, "/", m, "/", a, " n'est pas valide")
        else:
            print(j, "/", m, "/", a, " est valide")
    else:
        if j > 28:
            print(j, "/", m, "/", a, " n'est pas valide")
        else:
            print(j, "/", m, "/", a, " est valide")

