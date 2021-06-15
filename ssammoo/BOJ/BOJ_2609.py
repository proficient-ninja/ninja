import math

input_val = input().split()

to_int = []
left = set()
right = set()

for each in input_val :
    to_int.append(int(each))
    

for each in range(1, to_int[0] + 1):
    if to_int[0] % each == 0 :
        left.add(each)

for each in range(1, to_int[1] + 1):
    if to_int[1] % each == 0 :
        right.add(each)  


left_and_right = list(left & right)
left_and_right.sort()
measure = left_and_right[-1]
common_multi = int(to_int[0] * to_int[1] / measure) 

print(measure)
print(common_multi)