import sys
n = int(sys.stdin.readline())

for _ in range(n):
	money = int(sys.stdin.readline())
	for i in [25, 10, 5, 1]:
		print(money//i, end=' ')
		money = money%i