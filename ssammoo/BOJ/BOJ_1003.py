import sys

input_val = int(input())

dp_0 = [0] * 41
dp_1 = [0] * 41

dp_0[0] = 1
dp_1[1] = 1

for each in range(2, 41) :
    dp_0[each] = dp_0[each - 2] + dp_0[each - 1]
    dp_1[each] = dp_1[each - 2] + dp_1[each - 1]


for each in range(input_val):
    each_input = int(sys.stdin.readline())
    print(dp_0[each_input], dp_1[each_input])

