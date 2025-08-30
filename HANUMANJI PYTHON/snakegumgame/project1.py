'''
1 for snake
-1 for water
0 for gun
'''
import random
computer=random.choice([1,-1,0])
youstr=input("enter choice")
youDict={"s":1,"w":-1,"g":0}
reverseDict={1:"snake",-1:"water",0:"gun"}
you=youDict[youstr]
print(f"you chhose {reverseDict[you]} \n computer choose{reverseDict[computer]}")
if(computer==you):
   print("draw")
else:
    if(computer==1 and you==0):
        print("u win")
    elif(computer==-1 and you==0):
        print("u lose")
    elif(computer==1 and you==-1):
        print("u lose")
    elif(computer==0 and you==-1):
        print("u win")
    elif(computer==0 and you==-1):
        print("u win")
    elif(computer==0 and you==1):
        print("u lose")

    else:
         print("something is good")




