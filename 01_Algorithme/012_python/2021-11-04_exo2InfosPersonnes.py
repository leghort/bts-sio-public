'''
Exo 2 :
Ecrire un programme python qui, partant du fichier existant
'infosPersonnes.txt', l'ouvre en mode lecture "r", extrait chaque ligne
du fichier jusqu'à la fin de celui ci.

Pour chaque ligne extraite on récuperera l'age et le salaire et on
affichera l'age moyen ainsi que le salaire moyen des personnes.
'''

# Ouverture du fichier en mode lecture
ficInfos = open("infosPersonnes.txt", "r")
sommeAge = 0
sommeSalaire = 0

# NbPersonnes correspond aux nombre de lignes du fichier
nbPersonnes = 0

# Lecture du fichier
finFichier = False

while finFichier == False:
    ligne = ficInfos.readline()

    if ligne == "":
        finFichier = True
    else:
        print(ligne)
        
        elementsLigne = ligne.split(" ")
        # Extraire l'age
        age = int(elementsLigne[2])
        sommeAge = sommeAge + age
        salaire = float(elementsLigne[4])
        sommeSalaire = sommeSalaire + salaire
        nbPersonnes = nbPersonnes +1
        

print(" Age moyen des personnes ", sommeAge/nbPersonnes)
print(" salaire moyen des personnes ", sommeSalaire/nbPersonnes)

        
# Fermeture fichier
ficInfos.close()
