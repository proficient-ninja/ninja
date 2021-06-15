input = int(input())

count = 0
start_num = 666

while True :
    if "666" in str(start_num):
        count += 1
    if count == input :
        break
    start_num += 1

print(start_num)