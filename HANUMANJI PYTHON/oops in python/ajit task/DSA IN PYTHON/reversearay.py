# n=list(input("enter the array"))


# print(n[::-1])



# num= int(input("Enter the elements of list: "))
# list2=[]

# print(list2[::-1])


n=int(input("enter how many number you want to reverse"))
list=[]
for i in range(n):
    element=int(input(f"enter elemet {i+1}: "))
    list.append(element)
print("original list",list)
print("reversed list",list[::-1])
