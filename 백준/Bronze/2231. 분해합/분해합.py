import sys
n = int(sys.stdin.readline())

for i in range(1, n + 1):
    num = sum(map(int, str(i)))
    num_sum = i + num

    if i == n:
        print(0)
    if num_sum == n:
        print(i)
        break