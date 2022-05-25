#6047번문제
#정수 2개(a, b)를 입력받아 a를 2^b배 곱한 값으로 출력해보자.

a,b = input().split()
a = int(a)
b = int(b)
print(a*(2**b))

#or

print(a<<b)     # a * 2^b

