def printl(lala):
    for x in lala:
        print(x)

liste = [17, 38, 10, 25, 72]
liste.sort
print("1ere liste : ---------------------------------------")
printl(liste)
liste.append(12)
liste.sort(reverse=True)
print("2eme liste : ---------------------------------------")
printl(liste)
print("indice de 17 : ---------------------------------------")
print(liste.index(17))
print("3eme liste : ---------------------------------------")
liste.remove(17)
printl(liste)
print(liste[2:3])
print(liste[:2])
print(liste[3:])
print(liste[:])