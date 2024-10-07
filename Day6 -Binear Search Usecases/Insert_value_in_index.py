n=int(input("Enter no of elements in the list =="))
l=[int(input("Enter value==")) for i in range(n)]
key=int(input("Enter value  to be inserted =="))
def peak(l):
    low=0
    high=len(l)-1
    while low<=high:
        mid=(low+high)//2
        if (l[mid]==key):
            return mid+1
        elif l[mid]<key:
            low=mid+1
        else:
            high=mid-1
    return low
        
ans=peak(l)
print("key should be inserted in {0}".format(ans))

   