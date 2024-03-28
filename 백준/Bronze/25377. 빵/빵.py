import sys
n = int(sys.stdin.readline())

result = []
if n != 0:
    for _ in range(n):
        a, b = map(int, sys.stdin.readline().split())
        if a <= b:
            result.append(a + (b - a))

if len(result) == 0:
    print(-1)
else:
    print(min(result))