

n=int(input("Enter no of elements=="))
l=[int(input("Enter element ==")) for i in range(n)]
for i in range(len(l)):
    for j in range(len(l)-1):
        if(l[j]>l[j+1]):
            l[j],l[j+1]=l[j+1],l[j]
print(l)
            