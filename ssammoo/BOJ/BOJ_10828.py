import sys
input_num = int(sys.stdin.readline())

stack_arr =[]

for each in range(input_num):
    input_arr = sys.stdin.readline().split()
    len_stack = len(stack_arr)
    keyword = input_arr[0]

    if keyword == "push" :
        stack_arr.append(int(input_arr[1]))
    
    if keyword == "pop":
        if len_stack == 0 :
            print("-1")
        else :
            print(stack_arr.pop())
    
    if keyword == "size":
        print(len_stack)
    
    if keyword == "empty":
        if len_stack == 0 :
            print("1")
        else :
            print("0")
    
    if keyword == "top":
        if len_stack == 0 :
            print("-1")
        else :
            print(stack_arr[-1])
