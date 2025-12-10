num=int(input("enter the num "))
from math import sqrt
result=[]
for i in range(1,int(sqrt(num))+1):
    if num%i==0:
        result.append(i)
        if (i!=num//i):
            result.append(num//i)
result.sort()
print("factor of ",num,"are",result)
