pSeuil = 2.3
vSeuil = 7.41
pression=float(input("entrez la pression"))
volume=float(input("entrez le volume"))
if pSeuil<pression and vSeuil < volume:
  print("arret immédiate")
elif pSeuil<pression and vSeuil > volume:
  print("augmentation volume")
elif pSeuil > pression and vSeuil < volume:
    print("diminuer volume")
else:
    print("tout va bien")