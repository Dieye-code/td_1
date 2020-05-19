s = 0
while True:
    n = input("entrer le prix d'un article: ")
    while n.isdigit() == False:
        n = input("vous devez entrer un entier: ")
    n = int (n)
    s += n
    if n == 0:
        break
print("le Prix total est ",s)
