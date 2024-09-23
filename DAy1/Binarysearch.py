l=[9,8,7,6,5,4,3,2,1]
key=int(input("Enter value to search ==="))
low=0
high=len(l)-1
found=0
while(low<=high):
  mid=(low+high)//2
  if(l[mid]==key):
     print("key found at index {} ".format(mid))
     found=1
     break
  elif(l[mid]<key):
    high=mid-1
  else:
    low=mid+1
if(found==0):
  print("key not found in thelist")
