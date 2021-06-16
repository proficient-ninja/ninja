array_ea = int(input())

input_arr = []

for each in range(array_ea):
    x, y = map(int, input().split() )
    input_arr.append([y, x])


input_arr.sort()

for each in input_arr :
    print(f"{each[1]} {each[0]}")