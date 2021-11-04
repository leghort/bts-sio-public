'''
Exo 3 :
Toujours à partir du même fichier 'infosPersonnes.txt', qu'on ouvrira en
mode lecture, on créera un programme python qui contiendra :

    • une fonction de recherche 'recherchePersonne(nom)' qui à partir
    du nom passé en paramètre, récupere l'age et le salaire correspondant
    et affiche à l'écran le nom suivi de l'age et du salaire.
    Si la personne (nom) n'existe pas dans le fichier on affiche le
    message suivant : "Cette personne n'est pas enregistré !"
      
    • une fonction d'ajout 'addNewPerson()' des informations d'une nouvelle personne.
    On ouvrira donc, le fichier en mode append, on saisit les
    informations de la nouvelle personne qu'on enregistre dans le fichier.

    • une fonction 'intervalleAge(minAge, maxAge) permettant d'afficher les
     noms, prénoms age
     de chaque personne dont l'age est compris entre minAge et maxAge
     (bornes comprises).
    

'''
# Recherche d'une personne
def recherchePersonne(nom):
    # Ouverture du fichier en mode lecture
    ficInfos = open("infosPersonnes.txt", "r")

    # Lecture du fichier
    finFichier = False

    personneTrouvee = False

    while finFichier == False and personneTrouvee == False:
        ligne = ficInfos.readline()

        if ligne == "":
            finFichier = True
        else:
            elementsLigne = ligne.split(" ")
            if nom == elementsLigne[0]:
                age = elementsLigne[2]
                salaire = elementsLigne[4]
                print(nom+ " "+age +" " + salaire)

                personneTrouvee = True
            
    if personneTrouvee == False:
        print(" Cette personne n'existe pas dans le fichier!!")

    ficInfos.close()

# Ajout des infos d'une nouvelle personne
def addNewPerson():
    
    # Ouverture du fichier en mode append
    ficInfos = open("infosPersonnes.txt", "a")

    # Saisie des infos 
    nom = input("Entrez votre nom ")
    prenom = input("Entrez votre prenom ")
    age = int(input("Entrez votre age "))
    ville = input("Entrez votre ville ")
    salaire = float(input("Entrez votre salaire "))

    # Enregistrement des infos d'une personne
    ficInfos.write(nom+" "+prenom + " " + str(age)+" " + ville + " "+ str(salaire))
    ficInfos.write("\n")

    ficInfos.close()


# Prog principal

# appel fonction

# Recherches personnes
recherchePersonne("calvo")
recherchePersonne("Dupuis")
recherchePersonne("tata")

# Ajout nouvelles personnes
addNewPerson()
addNewPerson()





    
