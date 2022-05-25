#6095번 문제
#바둑판(19 * 19)에 n개의 흰 돌을 놓는다고 할 때,
#n개의 흰 돌이 놓인 위치를 출력하는 프로그램을 작성해보자.

d = [] #아무것도 없는 빈 리스트 만들기
for i in range(20):  # 리스트 안에 다른 리스트 추가해 넣기 (열)
    d.append([])
    for j in range(20):  #  d 안에 들어있는 각 리스트에 0을 20개 추가 (행)
        d[i].append(0)
        
n = int(input())
for i in range(n):
    x, y = map(int, input().split())    # 만약 x = 3  y = 4 이면,
    d[x][y] = 1                         # d[3]의 0이 4번째에 있는 곳 출력
    
for i in range(1, 20) :
    for j in range(1, 20) : 
        print(d[i][j], end=' ')  
    print()
