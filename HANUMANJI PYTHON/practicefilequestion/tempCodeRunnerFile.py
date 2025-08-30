# import lorem

# print(lorem.sentence())   # ek random sentence
# print(lorem.paragraph())  # ek random paragraph
# print(lorem.text())       # bada text

with open("practicefilequestion/lorem.txt","r") as f:
   data=f.read()
   if("python" in data):
      print("yes it is present")
   
   else: