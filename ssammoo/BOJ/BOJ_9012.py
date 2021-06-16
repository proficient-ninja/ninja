import sys
input_num = int(sys.stdin.readline())

for each in range(input_num):
    parentheis = sys.stdin.readline()
    parentheis_arr = []
    for each_parentheis in parentheis :
        parentheis_arr.append(each_parentheis)
    
    parentheis_arr.pop()

    arr_len =len(parentheis_arr)
    
    sum = 0

    for each in parentheis_arr :
        if each == "(":
            sum += 1
        elif each == ")" :
            sum -= 1
        if sum < 0 :
            print("NO")
            break

    if sum > 0 :
        print("NO")
    elif sum == 0 :
        print("YES")
    