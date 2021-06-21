import math

test_case = int(input())

for each in range(test_case) :
    data = list(map(int, input().split()))

    abs_x = abs(data[0]-data[3])
    abs_y = abs(data[1]-data[4])

    distance_1_2 = math.sqrt(abs_x ** 2 + abs_y ** 2)

    sum_r = data[2] + data[5]
    minus_r = abs(data[2] - data[5])

    if distance_1_2 == 0 :
        if data[2] == data[5] :
            print(-1)
        else :
            print(0)

    elif sum_r == distance_1_2 or minus_r == distance_1_2 :
        print(1)
    elif sum_r > distance_1_2 and minus_r < distance_1_2  :
        print(2)
    else :
        print(0)
