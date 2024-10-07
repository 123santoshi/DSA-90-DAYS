n=int(input("Enter no of elements in the list =="))
l=[int(input("Enter value==")) for i in range(n)]

def peak(l):
    low=0
    high=len(l)-1
    while low<high:
        mid=(low+high)//2
        if (l[mid]<l[mid+1]):
            low=mid+1
        else:
            high=mid
        return low
ans=peak(l)
print("index of peak element =={0} and element is {1}".format(ans,l[ans]))

   