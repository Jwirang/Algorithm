import sys
from collections import deque
n = int(sys.stdin.readline())

card_list = deque()
for i in range(1, n + 1):
    card_list.append(i)

for i in range(n):
    if len(card_list) == 1:
        print(card_list[0])
        break
    else:
        card_list.popleft()
        card_list.rotate(-1)