'''
Programme python qui demande a saisir un numéro de table de 
multiplication  (de 1 à 10) et qui affiche les résultats sous cette forme :
Ex si n = 6
6x1 =6
6x2 =12
..
6x10 = 60
Si le choix de la table est <1 ou >10 un message d'erreur est affiché indiquant de 
resaisir un numéro correct.
Apres chaque table de mutiplication affichée, le programme demande si l'on
 veut calculer une autre table de multiplication ;  si la réponse est 'O' on 
redemande à saisir un numéro de table et on affiche la nouvelle table.
Le programme se termine si on entre autre chose que 'O'.
'''

reponse = 'O'
while reponse == 'O':
    numTable = int(input("Entrez un numero de table"))

    while numTable <1 or numTable >10:
        print("numero table incorrect! resaisir..")
        numTable = int(input("Entrez un numero de table"))

    for i in range(1,11):
        print(numTable, "x", i, "= ", numTable*i)

    reponse = input("Voulez vous continuer ? : O  ou autre..")
                             
                             
