input_val = int(input())

arr = []

for each in range(1, input_val + 1) :
    number_arr = list(map(int, str(each)))
    sum_each = each + sum(number_arr)
    if sum_each == input_val :
        arr.append(each)


try :
    print(arr[0])
except :
    print(0)