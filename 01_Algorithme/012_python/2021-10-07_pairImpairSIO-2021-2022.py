'''
Programme python qui saisit N nombres et qui affiche si ce nombre est pair
ou impair.
Le programme s'arrete des qu'on saisit un nombre negatif
'''

# Booleen
encore = True

while encore == True:

    '''
    print("Saisir un nombre entier ")
    nb = input()
    nb = int(nb)
    '''
    # OU
    nb = int(input("Saisir un nombre entier "))

    # Test de coherence
    if nb < 0:
        print("Bye!!")
        encore = False
    else:
        # Test de la parite
        if nb %2== 0:
            print("Ce nombre est pair")
        else:
            print("Ce nombre est impair")

print("Fin Programme!!!")



            
        
