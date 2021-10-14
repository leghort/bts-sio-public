'''
V2
Ecrire un programme python qui saisit 2 nombres entiers de manière
continue tant que les 2 nombres saisis restent positifs.

Si au moins un des 2 nombres est négatif ou nul, le programme s'arrete.

Le traitement réalisé en dehors de ce cas consiste à afficher la somme
des 2 nombres si ces 2 nombres sont impairs, à afficher le produit de ces
2 nombres si les 2 sont pairs. 
Dans les autres cas on affiche la differences des 2 (soit nb1-nb2).
'''
stop = False

while stop == False :
    
    nb1 = int(input("Saisir a nouveau le premier nombre entier "))
    nb2 = int(input("Saisir a nouveau le 2eme nombre entier "))

    if nb1 >0 and nb2 >0:
        
        if nb1%2 == 1 and nb2%2 == 1 :
            print("somme = ", (nb1+nb2))
        elif nb1%2 == 0 and nb2%2 == 0 :
            print("produit = ", (nb1*nb2))
        else :
            print("difference = ", (nb1-nb2))
    else:
        stop = True
   
