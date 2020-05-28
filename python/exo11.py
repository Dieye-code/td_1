a = input("A : ")
while a.isdigit() == False:
    a = input("Vous devez entrer un entier : ")

o = input("Operation: ")

b = input("B : ")
while b.isdigit() == False:
    b = input("Vous devez entrer un entier : ")

a = int(a)
b = int(b)

if o=="+":
    print(a," + ",b," = ",a+b)
elif o=="-":
    print(a, " - ", b, " = ", a-b)
elif o == "*":
    print(a, " X ", b, " = ", a*b)
elif o == "/":
    if b==0:
		print("Impossible de diviser par 0")
	else:
		print(a, " / ", b, " = ", a//b)
else:
    print("Votre choix n'existe pas")
