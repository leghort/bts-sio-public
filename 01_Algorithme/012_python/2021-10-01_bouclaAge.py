age = int(input("Entrez un age:"))

while age <=0:
    print("age incoherent recommencez!!")
    age = int(input("Entrez un age:"))
print("Vous avez ", age, " ans")


# OU
fini = False

while fini == False:
    age = int(input("Entrez un age:"))
    if(age <=0):
        print("age incoherent recommencez!!")
    else:
        fini = true
print("Vous avez ", age, " ans")
