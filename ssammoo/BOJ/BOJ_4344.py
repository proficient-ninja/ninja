case_num = int(input())

for each_case in range(case_num) :
    list_for_num = list(map(lambda each : int(each), input().split(" ")))

    average = sum(list_for_num[1:]) / list_for_num[0]
    count = 0
   
    for count_person in list_for_num[1:] :
        if count_person > average :
            count += 1

    result = count/list_for_num[0]*100

    print(f"{result:.3f}%")
