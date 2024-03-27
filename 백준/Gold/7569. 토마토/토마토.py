import sys
from collections import deque

m, n, h = map(int, sys.stdin.readline().split())
arr = [[list(map(int, sys.stdin.readline().split())) for _ in range(n)] for _ in range(h)]

def bfs():
    global m, n, h
    q = deque()
    v = [[[0] * m for _ in range(n)] for _ in range(h)]

    cnt = 0
    for hi in range(h):
        for i in range(n):
            for j in range(m):
                if arr[hi][i][j] == 1:
                    q.append((hi, i, j))
                    v[hi][i][j] = 1
                elif arr[hi][i][j] == 0:
                    cnt += 1

    while q:
        ch, ci, cj = q.popleft()

        for dh, di, dj in ((0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1), (-1, 0, 0), (1, 0, 0)):
            nh, ni, nj = ch + dh, ci + di, cj + dj
            if 0 <= nh < h and 0 <= ni < n and 0 <= nj < m and v[nh][ni][nj] == 0 and arr[nh][ni][nj] == 0:
                q.append((nh, ni, nj))
                v[nh][ni][nj] = v[ch][ci][cj] + 1
                cnt -= 1

    if cnt == 0:
        return v[ch][ci][cj] - 1
    else:
        return -1

ans = bfs()
print(ans)
