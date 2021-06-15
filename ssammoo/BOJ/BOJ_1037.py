ea_num = int(input())
real_arr = input().split()
to_num_arr = []

for each in real_arr :
    to_num_arr.append(int(each))

to_num_arr.sort()

result = to_num_arr[0] * to_num_arr[-1]

print(result)