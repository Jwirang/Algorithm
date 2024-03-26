import sys
from cmath import inf
import heapq

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((c, b))

start, end = map(int, sys.stdin.readline().split())

q = [(0, start)]
dist = [inf] * (n + 1)

while q:
    z, x = heapq.heappop(q)
    if dist[x] < z:
        continue
    for cost, next in graph[x]:
        cost = cost + z
        if dist[next] > cost:
            dist[next] = cost
            heapq.heappush(q, [cost, next])
print(dist[end])