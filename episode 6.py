def checkvalue(line):
    words = line.split("\\")
    if words[2] > words[3]:
        return True
    return False

lala=input("un nom de fichier")
fichier = open(lala, "r")

Lines=fichier.readlines()
fichier.close()
for line in Lines :
    if checkvalue(line) :
        print(line)
