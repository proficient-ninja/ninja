import math

insert_val = input().split()

to_int = []
prime_arr = []

for each in insert_val:
    to_int.append(int(each)) 


for each in range(2, to_int[1] + 1):
    check_for_prime = 0
    for each_inner in range(2, int(math.sqrt(each))+1):
        if each % each_inner == 0:
            check_for_prime += 1
            break
    
    if check_for_prime == 0 :
        prime_arr.append(each)

for result in prime_arr:
    if to_int[0] <= result :
        print(result)


