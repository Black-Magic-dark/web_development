
word=["rupam","bad","donkey"]
with open("practicefilequestion/donkey.txt","r") as f:
    data=f.read()
    for string in word:
     data=data.replace(string,"*"*len(string))
with open("practicefilequestion/donkey.txt","w") as f:
    f.write(data)
