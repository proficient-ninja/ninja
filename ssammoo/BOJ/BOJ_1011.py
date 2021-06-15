import math

case_num = int(input())

for each in range(case_num):
    from_x, from_y = input().split()
    from_x = int(from_x)
    from_y = int(from_y)

    distance = from_y - from_x
    count = 0

    floor_root_dis = math.floor(math.sqrt(distance))
    source_num =floor_root_dis ** 2

    
    if distance > source_num and distance <= source_num + floor_root_dis :
        count = floor_root_dis * 2

    elif distance > source_num + floor_root_dis :
        count = floor_root_dis * 2 + 1

    elif distance == source_num :
        count = floor_root_dis * 2 - 1
    
    if distance < 4 : 
        count = distance
    
    print(count)