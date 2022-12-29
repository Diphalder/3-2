import numpy as np

n=int(input("enter number of input : "))
a=[]
for i in range(n):
    x=int(input())
    a.append(x)

a.sort()
print("sorted order = ",a)

value=int(input("enter value for search  = "))

low=0
hi=n-1
index=-1
while(low<=hi):
    mid= (hi+low)/2
    mid =int(mid)
    if(a[mid] == value):
        index=mid
        break
    elif(a[mid]<value):
        low=mid+1
    else:
        hi=mid-1


if(index!=-1):
    print("DATA FOUND")
    print("index=",index)
else:
   print("DATA NOT FOUND") 



