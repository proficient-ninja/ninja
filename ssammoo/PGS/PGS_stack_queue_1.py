def solution(progresses, speeds):
    
    queue = progresses
    speed_queue = speeds
    queue_count = 100
    count_list = []
    count = 0
    
    while queue_count >= 0 :
        if len(queue) == 0 :
            count_list.append(count)
            break
        if queue[0] >= 100 :
            queue.pop(0)
            speed_queue.pop(0)
            count += 1
            continue 
            
        if count > 0 :
            count_list.append(count)
            queue_count -= count
            
        len_num = len(queue)        
        for index in range(len_num) :
            queue[index] = queue[index] + speed_queue[index]
        
        count = 0

    
    return count_list