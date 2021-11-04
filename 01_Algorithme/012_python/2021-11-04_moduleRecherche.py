# Fonctions de recherche

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
