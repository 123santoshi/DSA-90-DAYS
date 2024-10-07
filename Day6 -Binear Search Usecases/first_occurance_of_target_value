n=int(input("Enter no of elements in the list =="))
l=[int(input("Enter value==")) for i in range(n)]
key=int(input("Enter key value =="))
low=0
output=-1
high=len(l)-1
while low<=high:
    mid=(low+high)//2

    if(l[mid]==key):
        output=mid
        high=mid+1
    elif l[mid]>key:
        high=mid-1
    else:
        low=mid+1
    
print("index of last occurance of target value==",output )
