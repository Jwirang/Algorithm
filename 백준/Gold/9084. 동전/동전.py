import sys
t = int(sys.stdin.readline())

result = []
for _ in range(t):
    n = int(sys.stdin.readline())
    n_list = sys.stdin.readline().split()
    m = int(sys.stdin.readline())

    dp = [0] * (m + 1)
    dp[0] = 1

    for i in n_list:
        for j in range(1, m+ 1):
            if j >= int(i) :
                dp[j] += dp[j - int(i)]

    print(dp[m])