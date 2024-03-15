import sys
n = int(sys.stdin.readline())
data = [sys.stdin.readline().strip() for i in range(n)]

for i in range(0, n):
    print(int(data[i].split()[0]) + int(data[i].split()[1]))
