import sys
n = int(sys.stdin.readline())
n_list = list(map(int,sys.stdin.readline().split()))

n_list.sort()

start = 0
end = n-1
min = sys.maxsize

while start < end:
    i = n_list[start] + n_list[end]
    if abs(i) < min:
        min = abs(i)
        result = [n_list[start], n_list[end]]
    if i < 0:
        start += 1
    elif i > 0:
        end -= 1
    else:
        break

print(result[0], result[1]) 