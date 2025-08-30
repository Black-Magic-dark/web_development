with open("practicefilequestion/this_copy.txt","r")as f:
   data1=f.read()
with open("practicefilequestion/this.txt","r")as f:
   data2=f.read()
if(data1==data2):
   print("yes same")
else:
   ("no")      