import math
import sys

nat_num = 123456
mul_num = 2 * nat_num

prime_arr = []


for each in range(2, mul_num + 1):
    prime_confirm = 0
    for each_prime in range(2, int(math.sqrt(each))+1):
        if each % each_prime == 0:
            prime_confirm += 1
            break
    if prime_confirm == 0 :
        prime_arr.append(each)

num = int(sys.stdin.readline())
while num != 0:
    count = 0
    for i in prime_arr:
        if num < i <= num * 2:
            count += 1
    print(count)
    num = int(sys.stdin.readline())

