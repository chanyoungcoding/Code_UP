#6075번 문제
#정수(0 ~ 100) 1개를 입력받아 0부터 그 수까지 순서대로 출력해보자.

a = int(input())

count = 0
while True:
    print(count)
    count += 1
    
    if count > a:
        break