import sys
num = int(sys.stdin.readline())

s = 1
for i in range(1, num+1):
    s *= i

print(s)