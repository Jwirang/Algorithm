import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))

result = 0

for i in range(n):
    result += max(b) * min(a)
    a.pop(a.index(min(a)))
    b.pop(b.index(max(b)))

print(result)