total_num = set(range(1, 10001))
non_self_numbers = set()

for each in total_num:
    for each_num in str(each) :
        each += int(each_num)
    non_self_numbers.add(each)

self_numbers = sorted(total_num - non_self_numbers)

for each in self_numbers :
    print(each)