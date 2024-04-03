import sys

n = int(sys.stdin.readline())
p = list(map(int, sys.stdin.readline().split()))

p.sort()
result = [0]
for i in range(len(p)):
    result.append(p[i] + result[-1])
print(sum(result))