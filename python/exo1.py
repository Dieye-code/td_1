a = input("entrer la valeur de a \t");

while a.isdigit() == False:
    a = input("vous devez entrer un enrier\t")
b= input("entrer la valeur de b \t")

while b.isdigit() == False:
    b = input("vous devez entrer un enrier\t");
a = int(a);
b = int (b);
c = 17 // 5;
print("Le quotient de la division de a par b est ", a // b);
print("Le reste de la division de a par b est ", a%b);
print("le ratio de ", a, " et ", b, " est ", round((b*100/a),2),"%")
