# def func(i,n):
#    if(i>n):
#     return
#    print(i)
#    func(i+1,n)
# func(1,5)
# def func2(i,n):
#     if(i<n):
#      return
#     print(i)
#     func2(i-1,n)
# func2(4,1) 




# ajit code

# def print_pattern(n):
#     if n > 5:
#         return
    
#     print(n)
#     print_pattern(n + 1)

#     if n < 5:
#         print(n)

# print(print_pattern(1))


def print_pattern(n, max_n=5):
    if n > max_n:
        return
    
    print(n)            # Print current number before recursion
    print_pattern(n + 1, max_n)  # Recursive call with next number
    print(n)            # Print current number again on return (unwinding)

print_pattern(1)
