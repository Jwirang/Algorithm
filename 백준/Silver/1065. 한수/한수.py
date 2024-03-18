import sys
n = int(sys.stdin.readline())

count = 0
if n < 100:
    print(n)
else: 
    for i in range(100, n + 1):
        num_list = list(map(int, str(i)))
        if num_list[0] - num_list[1] == num_list[1] - num_list[2]:
            count += 1

    print(99 + count)