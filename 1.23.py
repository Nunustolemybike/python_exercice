def compterMots(lala):
    a=dict()
    words=lala.split()
    for word in words:
        print(word)
        if word in a:
            a[word] +=1
        else:
            a[word] = 1
    return a

print(compterMots("je suis un lapin je mange des carottes"))
