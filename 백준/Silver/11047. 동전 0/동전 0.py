import sys

n, k = map(int, sys.stdin.readline().split())

pay_list = []

for _ in range(n):
    pay_list.append(int(sys.stdin.readline()))

pay_list.sort(reverse=True)

coin = 0
for i in pay_list:
    coin += k//i
    k = k%i
print(coin)