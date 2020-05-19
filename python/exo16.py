x = input("entrer la valeurde x: ")
while x.isdigit() == False:
    x = input("vous devez entrer un entier: ")
n = input("entrer la valeurde n: ")
while n.isdigit() == False:
    n = input("vous devez entrer un entier: ")

x = int(x)
n = int(n)
q = 0
r = x

while r>=n:
    r = r-n
    q = q+1

print("Le quotient de la division de ",x," par ",n," est ",q)

