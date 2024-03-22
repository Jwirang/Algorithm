import sys
n = int(sys.stdin.readline())

pay_list = []
for i in range(n):
    pay = int(sys.stdin.readline())

    if pay == 0:
        pay_list.pop(-1)
    else:
        pay_list.append(pay)

print(sum(pay_list))