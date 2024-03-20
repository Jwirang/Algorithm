import sys

# 요일을 담은 list a
a  = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
 #월별 총 일수를 담은 list, 
 # b[0]는 1월, b[1]는 2월, ..... b[11]는 12월의 총 한 달 일수
b = [31,28,31,30,31,30,31,31,30,31,30,31]
day = 0 

 # 입력값 받기 m:월 d:일
m, d = map(int, sys.stdin.readline().split()) 

 # 입력한 m의 그 전까지의 총 일수를 다 더한다.  
 # 1월이면 아무것도 더하지 않고, 3월이면 1월~2월까지의 일수를 더한다
for i in range (0, m-1) :
  day += b[i]

 # 요일은 a에서 (day + 입력 일수)를 7로 나눈 나머지값을 순서로 하는 값이다
answer = (day + d) %7
print(a[answer])