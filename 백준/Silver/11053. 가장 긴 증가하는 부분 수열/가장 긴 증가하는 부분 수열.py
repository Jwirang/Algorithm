import sys
n = int(sys.stdin.readline())
n_list = [0] + list(map(int, sys.stdin.readline().split()))

dp = [0] * (n + 1)

for i in range(1, n + 1):
    mx = 0
    for j in range(0, i):
        if n_list[i] > n_list[j]:
            mx = max(mx, dp[j])
    dp[i] = mx + 1

print(max(dp))