'''
Exercice V :
Une forêt initialement de 20 hectares (année 0) perd chaque année 10 % de sa surface ; dans le même temps ,elle augmente sa surface de 3 hectares.
Calculer sa surface dans 5 ans
Calculer sa surface dans 10 ans
Calculer sa surface dans 100 ans
Quelle est la limite de cette surface au bout d'un temps infini
'''

nbAnnees = int(input("Entrez un nombre d'annees: "))

surface = 20

for i in range(1, nbAnnees+1):
    surface = 0.9*surface +3
    
print("Surface a l'annee ", nbAnnees, " vaut ", surface, " hectares")
