# -------------------------------
# Listes necessaires au programme
# -------------------------------

# Fichier des employes hommes
ficHommes = open("salariesHommes.txt", "a")

# Fichier des employes femmes
ficFemmes = open("salariesFemmes.txt", "a")

# Fichier des employes dont le salaire est
# compris entre 1000 et 1500 euros
ficSalaireInf = open("salairesInf.txt", "a")

# Fichier des employes dont le salaire est
# superieur a 1500 euros
ficSalaireSup = open("salairesSup.txt", "a")

#--------------------------------------
# Saisie des informations des 5 employes

for i in range(1, 6):
    nom = input("Saisir un nom: ")
    prenom = input("Saisir un prenom: ")
    sexe = input("Saisir le genre (M/F): ")
    salaire = float(input("saisir un salaire: "))

    # Test du genre de l'employe
    if sexe == "M":
        ficHommes.write(nom)
        ficHommes.write(" ")
        ficHommes.write(prenom)
        ficHommes.write("\n")
    else:
        ficFemmes.write(nom)
        ficFemmes.write(" ")
        ficFemmes.write(prenom)
        ficFemmes.write("\n")

    # Test du salaire
    if salaire >= 1000 and salaire <= 1500:
        ficSalaireInf.write(nom)
        ficSalaireInf.write(" ")
        ficSalaireInf.write(prenom)
        ficSalaireInf.write("\n")
    elif salaire > 1500:
        
        ficSalaireSup.write(nom)
        ficSalaireSup.write(" ")
        ficSalaireSup.write(prenom)
        ficSalaireSup.write("\n")
        
ficHommes.close()
ficFemmes.close()
ficSalaireInf.close()
ficSalaireSup.close()


print(" Merci de votre cooperation!!!!")



    

    










    
