import time

# Horloge

def salut():
    print("Salut")

def bye():
    print("Bye")
    
encore = True;
sec = 0
minutes = 0
heures = 0

while encore:
    
    time.sleep(1)
    
    sec = sec+1
    if sec == 60:
        sec = 0

        minutes = minutes +1
        if minutes == 60:
            minutes = 0
            sec =0
            heures = heures +1
    print("H:",heures,"M:",minutes,"S:",sec)

    if sec%10 == 0:
        salut()
    if sec%15 == 0:
        bye()


