#6092번문제
#6092번 문제
#보 선생님은 수업을 시작하기 전에 이상한 출석을 부른다.
#선생님은 출석부를 보고 번호를 부르는데, 학생들의 얼굴과 이름을 빨리 익히기 위해 번호를 무작위(랜덤)으로 부른다.
#그리고 얼굴과 이름이 잘 기억되지 않는 학생들은 번호를 여러 번 불러 이름과 얼굴을 빨리 익히려고 하는 것이다.
#출석 번호를 n번 무작위로 불렀을 때, 각 번호(1 ~ 23)가 불린 횟수를 각각 출력해보자.
# n = 10       a = 1 3 2 2 5 6 7 4 5 9

n = int(input())    #개수를 입력받아 n에 정수로 저장   
a = input().split() #공백을 기준으로 잘라 a에 순서대로 저장

for i in range(n):  
    a[i] = int(a[i])
    
d = []  # d라는 이름의 빈 리스트 생성
for i in range(24):     # d[0] = 0, d[1] = 0, d[2] = 0, d[3] = 0 ....... d[23] = 0 으로 저장
    d.append(0)
    
for i in range(n):   # 번호를 부를 때마다, 그 번호에 대한 카운트 1씩 증가
    d[a[i]] += 1
    
for i in range(1,24):
    print(d[i], end=' ')   
    