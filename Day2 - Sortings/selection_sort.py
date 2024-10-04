n=int(input("Enter no of elements=="))
l=[int(input("Enter element ==")) for i in range(n)]
for i in range(len(l)):
    min_index=i
    for j in range(i+1,len(l)):
        if(l[min_index]>l[j]):
            min_index=j
    l[i],l[min_index]=l[min_index],l[i]
print(l)
            