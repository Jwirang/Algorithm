import sys

s = sys.stdin.readline().strip()
s_list = list(s)
a_count = int(sys.stdin.readline())
a = [sys.stdin.readline() for _ in range(a_count)]

dp = [0] * (len(s_list) + 1)
dp[0] = 1

for i in range(len(s_list) + 1):
    for j in a:
        j_len = len(j.strip())
        if dp[i - j_len] == 1 and s_list[i - j_len:i] == list(j.strip()):
            dp[i] = 1

if dp[len(s_list)]:
    print(1)
else:
    print(0)