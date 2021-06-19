N = int(input())

stack= [0] * N

count = 0

def checker(start_num) :
    for node in range(start_num) :
        if stack[start_num] == stack[node] or (start_num - node) == abs(stack[start_num] - stack[node]) :
            return False
    return True

def back_tracking_queen(start_num) :
    global count

    if start_num == N :
        count += 1
        return

    else :
        for node in range(N):
            stack[start_num] = node
            if checker(start_num):
                back_tracking_queen(start_num+ 1)
            
back_tracking_queen(0)

print(count)