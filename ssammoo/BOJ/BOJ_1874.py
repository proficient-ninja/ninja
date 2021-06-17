
repeat_val = int(input())

numbers_arr = [] # 1 ~ repeat

operations_arr = []

to_stack_num = 1

temp = True

for each in range(repeat_val):
    input_val = int(input())

    while to_stack_num <= input_val :
        numbers_arr.append(to_stack_num)
        operations_arr.append("+")
        to_stack_num += 1
    
    if numbers_arr[-1] == input_val :
        numbers_arr.pop()
        operations_arr.append("-")
    
    else :
        temp = False

if temp == False :
    print("NO")
else :
    for each in operations_arr :
        print(each)




