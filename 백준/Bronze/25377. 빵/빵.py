import sys

n = int(sys.stdin.readline())
#n_list = map(int, sys.stdin.readline().split())
result = []
for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    if a < b:
        print(b - a)
        result.append(b)

if len(result) == 0:
    print(-1)
else:
    print(min(result))