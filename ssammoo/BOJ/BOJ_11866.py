total_arr, K = map(int, input().split())

arr = []

for each in range(1, total_arr + 1) :
    arr.append(each)

save_yose = []
print("<", end="")
K_index = 0
while len(arr) > 1 :
    K_index = K_index + K
    if K_index > len(arr):
        K_index = K_index % len(arr)
        if K_index == 0 :
            K_index = K_index + len(arr)
    K_index = K_index - 1
    print(str(arr.pop(K_index)), end=", ")

print("{}>".format(str(arr.pop())))