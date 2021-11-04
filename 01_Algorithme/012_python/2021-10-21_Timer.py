import time

encore = True;
compteur = 0;
while encore:
    print(compteur)
    time.sleep(1)
    compteur = compteur+1

    if compteur == 10:
        encore = False

print("Bye!!!")

    
