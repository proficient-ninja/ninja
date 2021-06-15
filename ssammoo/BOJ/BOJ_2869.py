to_up, to_down, height = input().split()
to_up = int(to_up)
to_down = int(to_down)
height = int(height)

different_day = to_up - to_down
final_different = height - to_up

if final_different % different_day != 0 :
    day = 1 + (final_different//different_day +  1)
else :
    day = 1 + final_different//different_day

print(day)


""" 
sum_height = 0
days = 0

while sum_height <= height :
    sum_height = sum_height + to_up
    if sum_height >= height :
        days += 1
        break
    else :
        days += 1
        sum_height = sum_height - to_down
print(days) 

"""