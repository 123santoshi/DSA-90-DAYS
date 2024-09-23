l=[9,10,45,56,3,54,8,34,5]
for i in range(len(l)):
    for j in range(len(l)-1):
        if(l[j]>l[j+1]):
            l[j],l[j+1]=l[j+1],l[j]
print(l)
            