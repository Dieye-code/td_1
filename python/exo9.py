print("Heure de départ")
hd = input("H : ")
while hd.isdigit() == False:
    hd = input("vous devez entré un entier : ")
md = input("Mn : ")
while md.isdigit() == False:
    md = input("vous devez entré un entier : ")

print("Heure d'arrivé")
ha = input("H : ")
while ha.isdigit() == False:
    ha = input("vous devez entré un entier : ")
ma = input("Mn : ")
while ma.isdigit() == False:
    ma = input("vous devez entré un entier : ")

hd = int(hd)
md = int(md)
ha = int(ha)
ma = int(ma)

if ha<hd:
    ha += ha +24

h1 = hd*60+md
h2 = ha*60+ma

h1 = h2-h1

print("La durée de vol est ",h1//60,"H",h1%60,"Mn")
