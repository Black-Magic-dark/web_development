def fab(num):
    if (num==0) :
        return 0
    elif (num==1) :
        return 1
    else:
     return fab(num-1)+fab(num-2)
print(fab(4))