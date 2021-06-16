import sys

input_num = int(sys.stdin.readline())

stack_array = []

for each in range(input_num):
    input_value = int(sys.stdin.readline())
    if input_value == 0 :
        stack_array.pop()
    
    else :
        stack_array.append(input_value)

sum_total = sum(stack_array)

print(sum_total)