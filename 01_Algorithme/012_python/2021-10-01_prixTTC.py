pht = float(input("Saisir un prix HT: "))
print("Prix HT = ", pht)
montantTVA = pht*0.2
print("Montant TVA: ", montantTVA)
pttc = pht + montantTVA
print("Prix TTC = ", pttc, " euros")
