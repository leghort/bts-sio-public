'''
Exercice II :
Ecrire un programme python qui saisit 5 notes (de maths, histoire,...)  et qui calcule la 
moyenne de ces notes. 
Afficher la moyenne.

'''
# concatenation de 2 chaines
chaine1 = "Salut "
chaine2 = "comment vas tu?"
print(chaine1+chaine2)
somme = 0
for i in range(1,6):
    note = int(input("Saisir la note N° "+str(i) +": "))
    somme = somme + note

moyenne = somme/5
print("Moyenne = ", moyenne)
    
