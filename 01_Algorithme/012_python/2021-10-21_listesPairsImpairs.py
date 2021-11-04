# Programme Liste pair/impair

listePair = []
listeImpair = []

for i in range(1, 11):
    nb = int(input("Saisir un nombre"))

    if nb %2 == 0:
        listePair.append(nb)
    else:
        listeImpair.append(nb)
print(listePair)
print(listeImpair)
