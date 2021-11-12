# Dictionnaires

'''
Tableau dont le contenu est adressable par une clé
'''

# Creation d'un dictionnaire vide
dico1 = dict()
# OU
dico2 = {}

# Creation d'un dictionnaire initialisé
#                   cle     valeur
dicoFrancAnglais = {}
dicoFrancAnglais["Bonjour"] = "Good Morning"
dicoFrancAnglais["Aurevoir"] = "Bye"
dicoFrancAnglais["Lait"] = "Milk"

print(dicoFrancAnglais)
dicoFrancAnglais["Lait"] = "Viande"
print(dicoFrancAnglais)

print(dicoFrancAnglais["Bonjour"])

def f():
    print("salutvvvv")

def g():
    print("Au revoirwwwww")

dicFonc = {}
dicFonc["appelF"] = f()
dicFonc["appelG"] = g()

dicFonc["appelF"]
dicFonc["appelG"]

print(len(dicFonc))

# Supprimer un element
del dicoFrancAnglais["Aurevoir"]
print(dicoFrancAnglais)
print(len(dicoFrancAnglais))








