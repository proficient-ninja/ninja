input_num_val = int(input())

checker_num = 0
for each in range(input_num_val) :
    input_val = input()
    for each_index in range(len(input_val) - 1):
        if input_val[each_index] != input_val[each_index + 1]:
            if input_val[each_index] in input_val[each_index + 1:] :
                checker_num -= 1
                break
    checker_num += 1

print(checker_num)