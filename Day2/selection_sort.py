l=[9,10,45,67,78,90]
for i in range(len(l)):
    min_index=i
    for j in range(i+1,len(l)):
        if(l[min_index]>l[j]):
            min_index=j
    l[i],l[min_index]=l[min_index],l[i]
print(l)
            