import sys
n = int(sys.stdin.readline())

sum = 0
th = 0
for i in range(0, n + 1):
    sum += i
    th += i ** 3

print(sum)
print(sum ** 2)
print(th)