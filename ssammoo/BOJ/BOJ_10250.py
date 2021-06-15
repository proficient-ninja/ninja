import math

repeat_num = int(input())


for each in range(repeat_num):
    input_val = input().split()
    to_int = []
    for each_inner in input_val :
        to_int.append(int(each_inner))
    nth_floor = to_int[2] % to_int[0]
    if nth_floor == 0 :
        nth_floor = to_int[0]
    arc = math.ceil(to_int[2] / to_int[0])
    if arc <= to_int[1] :
        if arc < 10 :
            address = str(nth_floor) + "0" + str(arc)
        else :
            address = str(nth_floor) + str(arc)
        print(address)
