N = int(input())

dp_arr =[0] * 101

dp_arr[0] = 1
dp_arr[1] = 1
dp_arr[2] = 1
dp_arr[3] = 2
dp_arr[4] = 2

for each in range(5, 101) :
    dp_arr[each] = dp_arr[each - 1] + dp_arr[each - 5]

for each in range(N) :
    input_val = int(input())
    print(dp_arr[input_val - 1])