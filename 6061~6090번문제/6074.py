#6074번문제
#영문 소문자(a ~ z) 1개가 입력되었을 때,
#a부터 그 문자까지의 알파벳을 순서대로 출력해보자.

a =ord(input())
b = ord('a')

while b <= a :
    print(chr(b), end=" ")
    b += 1