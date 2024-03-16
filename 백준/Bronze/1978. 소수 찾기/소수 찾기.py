import sys
n = int(sys.stdin.readline())
data = [sys.stdin.readline().strip() for i in range(1)]

count = 0
for line in data:
    data_list = line.split()
    for num in data_list:
        num = int(num)
        if num < 2:
            continue
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            count += 1

print(count)