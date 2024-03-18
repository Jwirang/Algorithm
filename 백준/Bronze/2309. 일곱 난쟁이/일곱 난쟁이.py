import sys
import itertools
data = [int(sys.stdin.readline().strip()) for _ in range(9)]

per_list = itertools.permutations(data, 7)

for i in per_list:
    if sum(i) == 100:
        sevensort_list = list(i)
        break

sevensort_list.sort()

for i in sevensort_list:
    print(i)