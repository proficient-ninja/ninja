length, aim = map(int,input().split())

arr = list(map(int, input().split()))

aim_arr = []

for each in arr :
    for each_in in arr :
        for each_inin in arr :
            if each + each_in + each_inin <= aim and each != each_in and each != each_inin and each_in != each_inin:
                aim_arr.append(each + each_in + each_inin)
aim_arr.sort()
print(aim_arr[-1])