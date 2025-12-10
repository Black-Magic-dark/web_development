n=int(input("enter the number of elements"))
arr=[]           #empty list
for i in range(n) :
    element=int(input(f"element{i+1}:"))
    arr.append(element)
arr.sort()

target=int(input("enetr the target value "))
# target=arr[i]+arr[j]
i=0
j=n-1
found=False
while i<j:
      if (arr[i]+arr[j])==target:
        print("paair found:", arr[i], "and", arr[j])
        break
      elif(arr[i]+arr[j]<target):
        i+=1
      else:
         j-=1
      if  not found :
        print("not pair  found ")
        break






