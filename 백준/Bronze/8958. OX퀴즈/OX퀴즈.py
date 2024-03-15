import sys
n = int(sys.stdin.readline())
data = [sys.stdin.readline().strip() for i in range(n)]

for i in range(n):
    o = 0
    score = 0
    for result in data[i]:
        if result == 'O':
            o += 1
        else:
            o= 0
        score += o
    print(score)
