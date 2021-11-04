# Prog: Infos peronnes
'''
Ecrire un programme python qui saisit des informations concernant des 
personnes. Ces informations sont les suivantes :
    • Nom
    • Prénom
    • Age
    • Adresse (ville uniquement)
    • salaire

Le programme saisira autant d'individus que l'on  désire tant que l'on répond
à la question "voulez vous continuer ? (O/N)" ) par l'affirmative.

Les informations de chaque personne seront stockées dans un fichier
'infosPersonnes.txt' que l'on ouvrira en mode "a" (append)

les informations de chaque personne seront stockées dans ce fichier suivant
la syntaxe suivante :
Nom Prénom Age Ville salaire \n  (où \n représente un retour à la ligne dans
le fichier).

Une fois toutes les infos sauvegardées on fermera le fichier.
'''

# Booleen indiquant qu'on continue de saisir
nouvelleSaisie = True

# Creation du fichier en mode append
ficInfos = open("infosPersonnes.txt", "a")

while nouvelleSaisie == True:
    
    # Saisie des infos 
    nom = input("Entrez votre nom ")
    prenom = input("Entrez votre prenom ")
    age = int(input("Entrez votre age "))
    ville = input("Entrez votre ville ")
    salaire = float(input("Entrez votre salaire "))

    # Enregistrement des infos d'une personne
    ficInfos.write(nom+" "+prenom + " " + str(age)+" " + ville + " "+ str(salaire))
    ficInfos.write("\n")

    reponse = input("Voulez vous continuer (O/N) ")
    
    while reponse != "N" and reponse != "O":
        print("reponse incorrecte entrez un nouveau choix: ")
        reponse = input("Voulez vous continuer (O/N) ")
        
    if reponse == "N":
        nouvelleSaisie = False 

   # Fermeture fichier
ficInfos.close()
    

    








