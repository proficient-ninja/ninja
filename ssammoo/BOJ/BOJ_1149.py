import sys

N = int(input())

cost_arr = []

for each in range(N) :
    each_cost = list(map(int, sys.stdin.readline().split()))
    cost_arr.append(each_cost)
    
for cost_index in range(1, len(cost_arr)) :
    cost_arr[cost_index][0] = cost_arr[cost_index][0] + min(cost_arr[cost_index - 1][1], cost_arr[cost_index - 1][2])
    cost_arr[cost_index][1] = cost_arr[cost_index][1] + min(cost_arr[cost_index - 1][0], cost_arr[cost_index - 1][2])
    cost_arr[cost_index][2] = cost_arr[cost_index][2] + min(cost_arr[cost_index - 1][1], cost_arr[cost_index - 1][0])

print(min(cost_arr[len(cost_arr) - 1][0], cost_arr[len(cost_arr) - 1][1], cost_arr[len(cost_arr) - 1][2]))
