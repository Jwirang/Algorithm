import sys
from functools import cmp_to_key
n = int(sys.stdin.readline())

n_list = [list(map(int, sys.stdin.readline().split()))for _ in range(n)]
def compare(left, right):
    if left[1] == right[1]:
        if left[0] < right[0]:
            return -1
        else:
            return 1
    if left[1] < right[1]:
        return -1
    else:
        return 1

n_list.sort(key= cmp_to_key(compare))
result  = []
result.append(n_list[0][1])
for i in range(1, n):
    if result[-1] <= n_list[i][0]:
        result.append(n_list[i][1])

print(len(result))
