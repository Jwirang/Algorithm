import sys
import itertools
n, range = map(int, sys.stdin.readline().split())
data = list(map(int, sys.stdin.readline().strip().split()))

card_list = itertools.permutations(data, 3)
mylist = []
for i in card_list:
    if sum(i) <= range:
        mylist.append(sum(i))

print(max(mylist))