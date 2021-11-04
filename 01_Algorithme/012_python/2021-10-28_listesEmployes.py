# -------------------------------
# Listes necessaires au programme
# -------------------------------

# Liste des employes hommes
hommes = list()

# Liste des employes femmes
femmes = list()

# Liste des employes dont le salaire est
# compris entre 1000 et 1500 euros
salaireInf = []

# Liste des employes dont le salaire est
# superieur a 1500 euros
salaireSup = []

#--------------------------------------
# Saisie des informations des 5 employes

for i in range(1, 6):
    nom = input("Saisir un nom: ")
    prenom = input("Saisir un prenom: ")
    sexe = input("Saisir le genre (M/F): ")
    salaire = float(input("saisir un salaire: "))

    # Test du genre de l'employe
    if sexe == "M":
        hommes.append(nom)
        hommes.append(prenom)
    else:
        femmes.append(nom)
        femmes.append(prenom)

    # Test du salaire
    if salaire >= 1000 and salaire <= 1500:
        salaireInf.append(nom)
        salaireInf.append(prenom)
    elif salaire > 1500:
        salaireSup.append(nom)
        salaireSup.append(prenom)

# Afficher le cotenu des listes
print("Liste des hommes:",hommes)
print("Liste des femmes:",femmes)
print("Liste des salaires inf:",salaireInf)
print("Liste des salaires Sup:",salaireSup)

print(" Merci de votre cooperation!!!!")



    

    










    
