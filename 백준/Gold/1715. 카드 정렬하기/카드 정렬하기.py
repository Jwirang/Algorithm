import sys
import heapq
n = int(sys.stdin.readline())
x = [int(sys.stdin.readline()) for i in range(n)]

heapq.heapify(x)  # 리스트를 힙으로 변환

result = 0
while len(x) > 1:
    min1 = int(heapq.heappop(x))
    min2 = int(heapq.heappop(x))
    result += min1 + min2
    heapq.heappush(x, min1 + min2)

print(result)
