n=int(input("Enter no of elements in the list =="))
l=[int(input("Enter value==")) for i in range(n)]
target=int(input("Enter Target value=="))
def peak(l):
    low=0
    high=len(l)-1
    while low<=high:
        mid=(low+high)//2
        if (l[mid]==target):
            return mid-1
        elif l[mid]<target:
            low=mid+1
        else:
            high=mid-1
    return high
        
ans=peak(l)
print("Floor of a number near to the target is = {0}".format(l[ans]))

   