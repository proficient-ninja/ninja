import sys

N = int(input())

tri_arr = []

for each in range(N) :
    each_arr = list(map(int, sys.stdin.readline().split()))
    tri_arr.append(each_arr)

each_line_count = 2

for each_line_index in range(1, N) :
    for each_number_index in range(each_line_count) :
        if each_number_index == 0 :
            tri_arr[each_line_index][each_number_index] = tri_arr[each_line_index-1][each_number_index] + tri_arr[each_line_index][each_number_index]
        
        elif each_number_index == each_line_index :
            tri_arr[each_line_index][each_number_index] = tri_arr[each_line_index-1][each_number_index - 1] + tri_arr[each_line_index][each_number_index]
        
        else :
            val_1 = tri_arr[each_line_index][each_number_index] + tri_arr[each_line_index - 1][each_number_index -1]
            val_2 = tri_arr[each_line_index][each_number_index] + tri_arr[each_line_index - 1][each_number_index]
            max_val = max(val_1, val_2)
            tri_arr[each_line_index][each_number_index] = max_val
    
    each_line_count += 1

print(max(tri_arr[-1]))