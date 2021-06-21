input_equation = list(map(str,input().split("-")))

arr_for_sum = []

arr_for_sum.append(sum(list(map(int,input_equation[0].split("+")))))

for each in range(1, len(input_equation)):
    plus_sum = sum(list(map(int,input_equation[each].split("+"))))
    arr_for_sum.append(-plus_sum)


print(sum(arr_for_sum))    

