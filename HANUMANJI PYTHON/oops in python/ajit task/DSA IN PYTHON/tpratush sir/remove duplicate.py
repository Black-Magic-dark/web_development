n=int(input("enter the no. of elements"))
arr=[]
for i in range(n):
    elements=int(input(f"elements{i+1}"))
    arr.append(elements)
arr.sort()
i=0
j=1
unique=1
while(j<n):
    if(arr[i] !=arr[j]):
         unique+=1
         i=j
    j+=1     

    
print(arr)
print("no. of unique",unique)




