N = int(input())

time_arr = list(map(int, input().split()))

time_arr.sort()

total_time = 0

for each_index in range(N):
    total_time += sum(time_arr[:each_index + 1])

print(total_time)