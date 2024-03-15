import sys
n = int(sys.stdin.readline())
data = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]

for case in data:
    avg = (sum(case) - case[0]) / case[0]
    count = sum(1 for x in case[1:] if x > avg)
    print(f'{count/case[0] * 100:.3f}%')