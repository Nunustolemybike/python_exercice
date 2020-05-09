import re
chaine=str(input("entrez une chaine de carac"))
x=re.search("@[a-z0-9._-]{2,}\.[a-zA-Z]{0,3}$", chaine)
if (x):
  print("YES! We have a match!")
else:
  print("No match")
