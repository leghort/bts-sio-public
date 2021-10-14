'''
Exercice IV :
Un cycliste souhaite s'entrainer pour une compétition. Il prépare un programme 
d'entrainement de 3 semaines.
Le premier jour, il parcourt 30km puis il décide d'augmenter la distance
parcourue de 10km  chaque jour.
1) Ecrire un programme python qui calcule et affiche le nombre de kilometres
parcourus le 10eme jour d'entrainement.
De même pour le dernier jour d'entrainement.

2) Modifier le programme pour qu'il calcule le nombre total de
kilometres parcourus durant ce programme d'entrainement.
'''

# Reponse1
# Nombre de Km parcourus le 10 eme jour
# Distance 1er jour: 30km
dist = 30

numJour = int(input("Entrez un numero de jour: "))
for i in range(1,numJour):
    dist = dist +10

print("Distance parcourue au ", numJour , " jour", dist)

# Reponse2
# Distance 1er jour: 30km
dist = 30
distanceTotale = 30
for i in range(1,21):
    dist = dist +10
    distanceTotale = distanceTotale + dist

print("Distance totale parcourue ", distanceTotale)


