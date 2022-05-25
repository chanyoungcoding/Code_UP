# 6097문제
#6097번문제
#격자판의 세로(h), 가로(w), 막대의 개수(n), 각 막대의 길이(l),
#막대를 놓는 방향(d:가로는 0, 세로는 1)과
#막대를 놓는 막대의 가장 왼쪽 또는 위쪽의 위치(x, y)가 주어질 때,
#격자판을 채운 막대의 모양을 출력하는 프로그램을 만들어보자.

h, w = map(int,input().split())
n= int(input())


p =[]
p=[ [0 for i in range(w)] for j in range(h)]

for i in range(n):
    l,d,x,y = map(int,input().split())
    if d == 0:
        for k in range(l):
            p[x-1][y-1+k] = 1
    else:
        for k in range(l):
            p[x-1+k][y-1] = 1
            
for i in range(h):
    for j in range(w):
        print(p[i][j],  end=' ')
    print()