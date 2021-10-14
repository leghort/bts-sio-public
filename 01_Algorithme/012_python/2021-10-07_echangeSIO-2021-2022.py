# Programme python qui echange les valeurs de 2 variables

# Commentaire sur une ligne

'''
    commentaires multilignes
    ....
    ...
'''

# Prog principal
print("Entrez un 1er nombre: ")
a = input()
print("Entrez un 2eme nombre: ")
b = input()
print(a, "  ", b)

# Echange des valeurs
temp = a
a = b
b= temp
print(a, "  ", b)

# Conversion du type chaine de caracteres en entier
a = int(a)
b = int(b)
print(a+b)

