import sys
n = int(sys.stdin.readline())
n_list = list(map(int, sys.stdin.readline().split()))

m = int(sys.stdin.readline())

dp = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n - i):
        end = j + i

        if j == end: # 시작과 끝이 같으면 무조건 펠린드롬
            dp[j][end] = 1
        elif n_list[j] == n_list[end]:
            if j + 1 == end: 
                dp[j][end] = 1
            elif dp[j + 1][end - 1] == 1:
                dp[j][end] = 1

for q in range(m):
    a, b = map(int, sys.stdin.readline().split())
    print(dp[a - 1][b - 1])
