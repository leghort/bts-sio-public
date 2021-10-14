# Calcul surface avec retour
def surface(long, larg):
    s = long*larg

    return s

longueur = int(input("Entrez une longueur "))
largeur = int(input("Entrez une largeur "))
hauteur = int(input("Entrez une hauteur "))

volume = surface(longueur,largeur)*hauteur
print("Volume ", volume)
