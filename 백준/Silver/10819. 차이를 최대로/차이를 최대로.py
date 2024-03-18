import sys
import itertools
n = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().strip().split()))

data_list = list(itertools.permutations(data, n))

result = []
for i in data_list:
    addsum = 0
    for j in range(n - 1):
        addsum += abs(i[j] - i[j + 1])
    result.append(addsum)

print(max(result))