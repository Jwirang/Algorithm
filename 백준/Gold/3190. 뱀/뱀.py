import sys

n = int(sys.stdin.readline())
k = int(sys.stdin.readline())
k_list = [tuple(map(int, sys.stdin.readline().split())) for _ in range(k)]
l = int(sys.stdin.readline())
l_list = [sys.stdin.readline().split() for _ in range(l)]

l_table = [0] * (10001)
for sec,turn in l_list:
    l_table[int(sec)] = turn

di, dj = [-1, 0, 1, 0], [0, 1, 0, -1]
dr = 1
snake = [(1,1)]
ans = 0

while True:
    ans += 1
    ci, cj = snake[0]
    ni, nj = ci+di[dr], cj+dj[dr]

    if 1 <= ni <= n and 1 <= nj <= n and (ni,nj) not in snake:
        snake.insert(0, (ni,nj))
        if (ni,nj) in k_list:
            k_list.remove((ni, nj))
        else:
            snake.remove((snake[-1]))
        
        if l_table[ans] == 'D':
            dr = (dr+1)%4
        elif l_table[ans] == 'L':
            dr = (dr+3)%4
    else:
        break

print(ans)
