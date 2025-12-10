def selectionsort(num):
    n=len(num)
    for i in range(0,n):
        mid_index=i
        for j in range(i+1,n):
            if num[j]< num[mid_index]:
                mid_index=j
        num[i],num[mid_index]= num[mid_index],num[i]  
    return num       
print(selectionsort([45,12,52,10]))