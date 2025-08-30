# import lorem

# print(lorem.sentence())   # ek random sentence
# print(lorem.paragraph())  # ek random paragraph
# print(lorem.text())       # bada text

with open("practicefilequestion/lorem.txt","r") as f:
   lines=f.readlines()
   lineno=1
   
for line in lines:
#    data=f.read()
   if("python" in line):
      print("yes it is present")
      print(lineno)
      break
   
   else:
      ("no")   