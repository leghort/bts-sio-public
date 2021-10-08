"""
Saisie N nombre qui affiche si ce nombre est pair ou impair.
Le programme s'arrete des qu'on saisit un nombre négatif
"""

i = True

while i == True:
    """
    print("Saisi un nombre entier")
    nb = input()
    nb = int(nb)
    """
    # OU
    nb = int(input('Saisie un nombre entier :'))
    # test de coherence
    if nb < 0:
        print("Bye!!")
        i = False
    else:
        # Test de la parite
        if nb %2== 0:
            print("pair"+ '\n')
        else:
            print("impaire"+1 '\n')