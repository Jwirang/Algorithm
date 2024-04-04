import sys
t = int(sys.stdin.readline())

for i in range(t):
	n, m = map(int,sys.stdin.readline().split())
	result = 0
	for a in range(1, n):
		for b in range(a+1, n):
			t = a * a + b * b + m
			if t % (a * b) == 0:
				result += 1
	print(result)