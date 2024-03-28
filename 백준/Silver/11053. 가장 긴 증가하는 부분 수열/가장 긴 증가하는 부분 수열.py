import sys
n = int(sys.stdin.readline())
n_list = list(map(int, sys.stdin.readline().split()))

result = [1] * n
count = 0
for i in range(1, n):
    for j in range(i):
        if n_list[i] > n_list[j]:
            result[i] = max(result[i], result[j] + 1)

print(max(result))