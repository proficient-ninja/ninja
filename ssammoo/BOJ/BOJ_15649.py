n, m = map(int, input().split())

stack = []

def back_tracking() :
    if len(stack) == m :
        print(*stack)
        return

    for each in range(1, n + 1):
        if each in stack :
            continue
        stack.append(each)
        back_tracking()
        stack.pop()

back_tracking()