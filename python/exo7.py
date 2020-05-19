montant = input("Entrer le montant a decomposér : ")
while montant.isdigit() == False:
    montant = input("vous devez entré un entier : ")
montant = int(montant)

m20 = montant//20
montant = montant%20
m10 = montant //10
montant = montant%10
m5 = montant // 5
montant = montant%5
m2 = montant // 2
m1 = montant%2

print("Le montant ",montant," est composé de :")
print(m20," billets de 20 euros")
print(m10," billets de 10 euros")
print(m5," billets de 5 euros")
print(m2, " piece de 2 euros")
print(m1," piece de 1 euros")
