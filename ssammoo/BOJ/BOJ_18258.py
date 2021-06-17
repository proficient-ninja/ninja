import sys
from collections import deque
repeat_val = int(sys.stdin.readline())

queue = deque([])

for repeat in range(repeat_val):
    command_str = sys.stdin.readline()
    command_arr = list(command_str.split())
    command_key = command_arr[0]

    if command_key == "push" :
        queue.append(int(command_arr[1]))

    if command_key == "pop" :
        if len(queue) == 0 :
            print("-1")
        else :
            print(queue.popleft())
    
    if command_key == "size" :
        print(len(queue))
    
    if command_key == "empty":
        if len(queue) == 0 :
            print("1")
        else : 
            print("0")
    
    if command_key == "front" :
        if len(queue) == 0 :
            print("-1")
        else :
            print(queue[0])
    
    if command_key == "back" :
        if len(queue) == 0 :
            print("-1")
        else :
            print(queue[-1])

