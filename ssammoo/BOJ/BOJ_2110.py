import sys

N, C = map(int, sys.stdin.readline().split())

house_arr = []

for each in range(N) :
    house_arr.append(int(sys.stdin.readline()))
house_arr.sort()

start = 1 # 최소 거리간격
end = house_arr[-1] - house_arr[0]
result = 0

while start <= end :
    mid = (start + end) // 2 # 단위 간격
    each_min = house_arr[0]
    count = 1

    for each_index in range(1, len(house_arr)) :
        if house_arr[each_index] >= (mid + each_min) :
            count += 1
            each_min = house_arr[each_index]
    
    if count >= C :
        start = mid + 1
        result = mid
    else :
        end = mid - 1
print(result)