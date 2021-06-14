input_value = int(input()) # 0 < <=99
repeat_value = input_value

result = 0
confirm = True

while confirm == True :
    repeat_10 = repeat_value // 10
    repeat_1 = repeat_value % 10
    repeat_plus = (repeat_10 + repeat_1) % 10

    result += 1
    repeat_value = repeat_1 * 10 + repeat_plus

    if repeat_value == input_value :
        confirm = False

print(result)