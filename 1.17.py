a="ellse"
g=0
for i in range(len(a)//2):
    if a[i] != a[-i-1]:
        g=g+1

if g>0 :
    print("ce nest pas un palindrome")
else:
    print("c'est un palindrome")

