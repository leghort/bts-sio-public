'''
Exercice III :
Ecrire un programme python qui saisit autant de  notes que l'on désire
(de maths, histoire,...) et qui calcule la moyenne de ces notes.
La saisie des notes s'arrete dès lors que la dernière a une valeur négative.
Afficher la moyenne et le nombre de notes saisies.
'''

stopSaisie = False

# Nombre de notes
nbNotes = 0

somme = 0

while stopSaisie == False:
    note = int(input("Saisir une note "))

    if note >= 0:
        somme = somme + note
        nbNotes = nbNotes+1
    else:
        stopSaisie = True

# Calcul de la moyenne
moyenne = somme/nbNotes

print("La moyenne vaut ", moyenne, "Nb notes saisies ", nbNotes) 

