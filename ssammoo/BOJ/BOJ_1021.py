queue_len, target_len = map(int, input().split())

target_arr = list(map(int, input().split()))

queue = []

count = 0

for each in range(1, queue_len + 1 ) :
    queue.append(int(each))

for target in target_arr :
    queue_half_index = (len(queue) - 1) // 2 
    target_index = queue.index(target)
    if queue_half_index >= target_index :
        while True:
            if queue[0] == target :
                queue.pop(0)
                break
            
            else :
                queue.append(queue.pop(0))
                count += 1
    else :    
        while True:
            if queue[0] == target :
                queue.pop(0)
                break
            else:
                queue.insert(0, queue.pop())
                count += 1
print(count)
