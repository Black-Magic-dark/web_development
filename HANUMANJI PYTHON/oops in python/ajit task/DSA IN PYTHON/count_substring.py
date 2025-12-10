str=input("enter the strinh")
myset=set()
# set()             built in set 
n=len(str)
for i in range(0,n):
    st=""
    for j in range(i,n):
        st+=str[j]
        myset.add(st)
print(len(myset)+1)
print(myset)