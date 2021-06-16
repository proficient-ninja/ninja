def top_of_hanoi (n, first, second, third):
    if n == 1 :
        total_num.append(first + " " + third)
        return 
    top_of_hanoi(n - 1, first, third, second)
    total_num.append(first + " " + third)
    top_of_hanoi(n - 1, second, first, third)


total_num = []
input_val = int(input())
top_of_hanoi(input_val, "1", "2", "3")
print(len(total_num))

for each in total_num:
    print(each)