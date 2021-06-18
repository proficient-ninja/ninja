n, m = map(int, input().split())

stack = []

def back_tracking(start_num) :
    if len(stack) == m :
        print(*stack)
        return

    for each in range(1, n + 1):
        if each in stack :
            continue
        if start_num <= each :
            stack.append(each)
            back_tracking(each)
            stack.pop()        

back_tracking(1)