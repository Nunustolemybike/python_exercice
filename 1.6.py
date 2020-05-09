import re
chaine=str(input("entrez une chaine de carac"))
x=re.search("@.*com$", chaine)
if (x):
  print("YES! We have a match!")
else:
  print("No match")
