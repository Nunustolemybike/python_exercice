x=int(input("entrez un nombre"))
fichier = open("data.txt", "a")
fichier.write("alala@alal.com")
a=1
while a < x :
    a = a + 1
    fichier.write("\nlala")

fichier.close()
