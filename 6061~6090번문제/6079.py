#6079번문제
#1, 2, 3 ... 을 계속 더해 나갈 때,
#그 합이 입력한 정수(0 ~ 1000)보다 같거나 작을 때까지만
#계속 더하는 프로그램을 작성해보자.

n = int(input())
sum = 0

for a in range(0, 1001):
    sum += a
    
    if (sum >= n):
        print(a)
        break
