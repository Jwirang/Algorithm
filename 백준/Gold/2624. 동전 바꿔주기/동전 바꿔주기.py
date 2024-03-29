import sys
T = int(sys.stdin.readline())
k = int(sys.stdin.readline())
coin = [[0, 0]]
dp = [[0 for _ in range(T+1)] for _ in range(k+1)]
for _ in range(k):
    x, y = map(int, sys.stdin.readline().split())
    coin.append([x, y])

dp[0][0] = 1
for i in range(1, k+1):
    val, cnt = coin[i]
    for j in range(T+1):
        dp[i][j] = dp[i-1][j]
        for v in range(1, cnt+1):
            if j-v*val >= 0:
                dp[i][j] += dp[i-1][j-v*val]
            else:
                break

print(dp[k][T])