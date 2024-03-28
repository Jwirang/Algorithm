import sys
n = int(sys.stdin.readline())

n_list = [0] * 1000001
n_list[1] = 1
n_list[2] = 2

for i in range(3, n + 1):
    n_list[i] = (n_list[i-1] + n_list[i-2]) % 15746
print(n_list[n])