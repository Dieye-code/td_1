def nbl(n):
    if(n<=1):
        return 2
    else:
        return nbl(n-1)+nbl(n-2)
print("Dans 12 mois nous aurons ",nbl(12))

nbM = 0
nbm = 2
i=0


while nbm+nbM<1000000000:
    i = i+1
    n = nbM
    nbM = nbm+nbM
    nbm = n
print("c'est dans ", i," mois que le nombre de lapins va depasser 1 millard")

