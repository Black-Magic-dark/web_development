# def greet():
#     print("rupam")
#     greet()
# greet()

# head recursion 
# count=0
# def func():
#     global count
#     if count==5:
#         return
#     print("xyz")
#     count+=1
#     func()
# func()



# tail recurdsion 

count=0
def func():
    global count
    if count==5:
        return
    count+=1
    func()
    print("xyz")
func()


