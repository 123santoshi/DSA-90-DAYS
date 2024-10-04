n=int(input("Enter no of elements=="))
l=[int(input("Enter element ==")) for i in range(n)]
key=int(input("Enter key value to search=="))
found=0
for i in l:
    if(i==key):
        print("Key found in the list at index {}".format(l.index(i)))
        found=1
        break
if(found==0):
    print("Key not found in the list")
