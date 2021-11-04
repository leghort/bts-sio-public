# Tableaux - Listes en python

# Creation d'une liste vide
# 2 methodes
maliste1 = []
maliste2 = list();

# Creation d'une liste non vide
maListe3 = ["Bonjour", 3.14, 45, 'A']

# Taille d'une liste fonction len()
print("taille de la liste maliste3: ", len(maListe3))

# Afficher le contenu d'une liste
for i in range(0, len(maListe3)):
    print(maListe3[i], " ")

# Ajouter un element a la liste fonction append
print(maliste1)
maliste1.append("salut")
maliste1.append(8)
print(maliste1)

# Enlever un element de la liste fonction remove
# en specifiant l'element a supprimer
maListe3.remove(3.14)
print(maListe3)

# Enlever un element de la liste fonction delete ou del
# en specifiant son indice dans la liste
del maListe3[1]
print(maListe3)

maListe4 = [1,2,3]
maliste1.append(maListe4)
print(maListe1)








