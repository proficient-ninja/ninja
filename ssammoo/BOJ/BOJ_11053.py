N = int(input())

get_arr = list(map(int, input().split()))

dp = [0 for each in range(N)]

for each in range(N) :
    for each_inner in range(each) :
        if get_arr[each] > get_arr[each_inner] and dp[each] < dp[each_inner] :
            dp[each] = dp[each_inner]
    dp[each] += 1

print(max(dp))
