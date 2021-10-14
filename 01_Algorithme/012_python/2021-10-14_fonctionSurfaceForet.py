# Fonctions en python

# Definition de la fonction surfaceForet
def surfaceForet(nbAns):
    surface = 20

    for i in range(1, nbAns+1):
        surface = 0.9*surface +3
    
    print("Surface a l'annee ", nbAns, " vaut ", surface, " hectares")


nbAnnees = int(input("Entrez un nombre d'annees: "))
# Appel de la fonction
surfaceForet(nbAnnees)
