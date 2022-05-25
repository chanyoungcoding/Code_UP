#6064번문제
#입력된 세 정수 a, b, c 중 가장 작은 값을 출력하는 프로그램을 작성해보자.
#단, 3항 연산을 사용한다.

a,b,c = input().split()
a = int(a)
b = int(b)
c = int(c)

print(min(a,b,c))

#or
#정석

a, b, c = map(int, input().split())
x = a if a < b else b
y = x if x < c else c
print (y)
