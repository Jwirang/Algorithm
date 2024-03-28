import sys
n = int(sys.stdin.readline())

n_list =[]
n_list.append(0)
n_list.append(1)

for i in range(n - 1):
    n_list.append(n_list[-1] + n_list[-2])

print(n_list[-1])