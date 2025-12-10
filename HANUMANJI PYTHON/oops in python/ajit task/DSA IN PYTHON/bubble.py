def bubblesort(num):
    n=len(num)
    for i in range(n-2,-1,-1):
        for j in range(0,i+1):
            if num[j]>num[j+1]:
             num[j],num[j+1] =num[j+1],num[j]
    return  num
print(bubblesort([152,625,85,96]))  