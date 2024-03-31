import sys
n, k = map(int, sys.stdin.readline().split())

money_list = [int(sys.stdin.readline()) for _ in range(n) ] 

dp = [float('inf')] * (k + 1)
dp[0] = 0

for i in money_list:
    for j in range(i, k + 1):
        dp[j] = min(dp[j], dp[j - i] + 1)

if dp[k] == float('inf'):
    print(-1)
else:
    print(dp[k])