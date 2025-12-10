num=list(map(int,input("enter thr number")))

largest=float("-inf")
s_largest=float("-inf")
n=len(num)
for i in range(0,n):
    if num[i]>largest:
        s_largest=largest
        largest=num[i]
    elif num[i]>s_largest and num[i]!=largest:
        s_largest=num[i]
    
print("second largest number is",s_largest)