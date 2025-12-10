num=int(input("enter the num "))
total=0
temp=num
nod=len(str(num))
while num>0:
    ld=num%10
    total=total+(ld**nod)
    num=num//10
if(temp==total):
   print(temp,"is armstrong")
else:
    print(temp,"no armstrong")
