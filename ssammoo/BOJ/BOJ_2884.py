hour_val, minute_val = input().split()

hour = int(hour_val)
minute = int(minute_val) - 45

if minute < 0 :
    minute = 60 + minute
    hour = hour - 1
    if hour < 0 :
        hour = 24 + hour



print(hour, minute)