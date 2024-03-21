import sys
import heapq
n = int(sys.stdin.readline())
x = [sys.stdin.readline().split() for i in range(n)]

x_list =[]
for i in x:
    if i[0] == '0':
        if len(x_list) == 0:
            print(0)
        else:
            print(-heapq.heappop(x_list))
    else:
        heapq.heappush(x_list, - int(i[0]))
