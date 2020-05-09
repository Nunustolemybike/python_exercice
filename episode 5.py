liste=["\b\t80cm\t60cm\n","\b\t81cm\t51cm\n","\b\t105cm\t145cm\n"]
for x in liste :
    words=x.split()
    if words[1]>words[2]:
        print(words)