N, K = map(int, input().split())

value_arr = []

for each in range(N) :
    input_val = int(input())
    value_arr.append(input_val)



coin_count = 0

for coin_val_index in range(len(value_arr) -1, -1, -1) :
    if K < value_arr[coin_val_index] :
        continue

    else :
        remain = K % value_arr[coin_val_index]
        coin_count += K // value_arr[coin_val_index]
        K = remain

        if N == 0 :
            break

print(coin_count)

