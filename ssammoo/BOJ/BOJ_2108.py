import sys
from collections import Counter

input_command_num = int(input())

arr = []

for each in range(input_command_num) :
    input = int(sys.stdin.readline())
    arr.append(input)

arr.sort()

numbers = Counter(arr).most_common()

arithmetic_mean = round((sum(arr) / len(arr)))
middle_value = arr[len(arr) // 2]


print(arithmetic_mean)
print(middle_value)

if len(numbers) > 1 :
    if numbers[0][1] == numbers[1][1] :
        print(numbers[1][0])
    else :
        print(numbers[0][0])
else :
    print(numbers[0][0])

print(arr[-1]-arr[0])