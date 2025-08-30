f=open("practice/practicefilequestion/file.txt","r")
data=f.read()
if("tehudk3d" in data):
   print("yes present")
else:
   print("no")   
# print(data)
f.close()