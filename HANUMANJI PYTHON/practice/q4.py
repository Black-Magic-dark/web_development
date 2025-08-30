# import os
# cwd=os.getcwd()
# print("current working directory",cwd)
# import os
# def current_path():
#     print("current working directory before")
#     print(os.getcwd())
#     print()
#     current_path()
#     os.chdir('../')
#     current_path()

# import os
# directory_path='/New Volume(C:)'
# content=os.listdir(directory_path)
# for item in content:
#     print(item)
# import os 
# path = "/"
# dir_list = os.listdir(path) 
# print("Files and directories in '", path, "' :") 
# print(dir_list)


# e= True or False
# print(e)

# name="rupa"
# mom="jit"
# print(f"dab andmdek {name} {mom}")
# l1=[1,85,96,47,0]
# l1.sort(reverse=True)
# print(l1)
# b=["gst","hlo", 6,8]
# # a=b.count(8)
# # print(b.count(6))
# # c=len(b)
# # print(c)


# dic={
#     "kuuta":"dog",
#     "madad":"help"
# }
# find=input("enteer word u ant to know:")
# if find  in dic:
#     print(dic[find])
# elif find in dic.values():
#        for k,v in dic.items():
#              if v ==find:
#                    print(k)
#                    break
#              else:
#                print("Not found")

# # print(dic[find])
# s=set()
# s.add(20)
# s.add(20.0)
# s.add('20')
# print(s)
# print(len(s))
# set={}
# # print(type(set))
# # a=input("enter name of subject ")
# m1=int(input("enter matrks "))
# # b=input("enter name of subject ")
# m2=int(input("enter matrks "))
# # c=input("enter name of subject ")
# m3=int(input("enter matrks "))
# total_percent=((m1+m2+m3)/300)*100
# if(total_percent>=40 and m1>=33 and m2>=33 and m3>=33):
#     print("u r pass", total_percent)
# else:
#     print("fail",total_percent)

post=input("enter the post")
if("rupam".lower() in post.lower()):
    print("yes rupam is present in post")
else:
    print("no")    

num=int(input("enter num"))
i=1
sum=0
for i in range(i<=num):
sum=sum+i
print(sum)
