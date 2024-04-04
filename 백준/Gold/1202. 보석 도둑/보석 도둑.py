import sys
import heapq

n, k = map(int, sys.stdin.readline().split())
bosuck = []
for _ in range(n):
    heapq.heappush(bosuck, list(map(int, sys.stdin.readline().split())))
bags = []
for _ in range(k):
    bags.append(int(sys.stdin.readline()))
bags.sort()

answer = 0
tmp_bosuck = []
for bag in bags:
    while bosuck and bag >= bosuck[0][0]:
        heapq.heappush(tmp_bosuck, -heapq.heappop(bosuck)[1])
    if tmp_bosuck:
        answer -= heapq.heappop(tmp_bosuck)
    elif not bosuck:
        break
print(answer)