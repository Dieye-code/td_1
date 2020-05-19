import math;
r = input("Entrer le rayon du cercle : ");
while r.isdigit() == False:
    r = input("Vous devez entrer un entier : ");
r = int(r);

p = 8*r*math.atan(1);
s = 4* r**2 * math.atan(1);

print(" le perimetre du cercle est ", round(p,2))
print(" la surface du cercle est ", round(s,2))
