#6087번문제
#1부터 입력한 정수까지 1씩 증가시켜 출력하는 프로그램을 작성하되,
#3의 배수인 경우는 출력하지 않도록 만들어보자.

num = int(input())

for a in range(1, num+1):
    if a%3 == 0:
        continue
    print(a, end=" ")
