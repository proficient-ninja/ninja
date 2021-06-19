n = int(input())

stair = [0] * 300

for each in range(n) :
    stair[each] = int(input())

dp = [0] * 300

dp[0] = stair[0]
dp[1] = stair[0] + stair[1]
dp[2] = max(stair[2] + stair[0], stair[2] + stair[1] )

for each in range(3, n) :
    dp[each] = max(dp[each - 3] + stair[each - 1] + stair[each], dp[each - 2] + stair[each])

print(dp[n - 1])
