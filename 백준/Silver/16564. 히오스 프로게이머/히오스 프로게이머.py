import sys
n, k = map(int,sys.stdin.readline().split())
n_lsit = [int(sys.stdin.readline())for _ in range(n)]

start = min(n_lsit)
end = start + k
result = 0

while start <= end:
    mid = (start + end) // 2

    hap = 0
    for i in n_lsit:
        if mid > i:
            hap += (mid - i)
    if hap <= k:
        start = mid + 1
        result = max(mid,result)
    else:
        end = mid - 1

print(result)