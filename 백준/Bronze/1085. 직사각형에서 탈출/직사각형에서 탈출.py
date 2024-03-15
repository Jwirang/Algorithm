x, y, w, h = map(int, input().split())

t = min(x, w - x)

s = min(y, h - y)

print(min(t, s))
