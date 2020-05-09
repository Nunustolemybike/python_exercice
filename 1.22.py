import re
def checkmail(lala):
    x=re.search("@[a-z0-9._-]{2,}\.[a-zA-Z]{0,3}$", lala)
    if (x):
        print("YES! We have a match!")
    else:
        print("No match")

fichier = open("data.txt", "r")
Lines=fichier.readlines()
fichier.close()
for line in Lines :
    checkmail(line)

