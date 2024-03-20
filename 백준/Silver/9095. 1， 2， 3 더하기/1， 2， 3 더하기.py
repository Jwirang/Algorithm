import sys
n = int(sys.stdin.readline())
n_lsit = [int(sys.stdin.readline().strip())for _ in range(n)]

cnt = [0,1,2,4]
for i in range(4,11):
	cnt.append(cnt[i-1] + cnt[i-2] + cnt[i-3])

for i in n_lsit:
	print(cnt[i])