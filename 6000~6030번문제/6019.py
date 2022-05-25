#6019번 문제
#"연도.월.일"을 입력받아 "일-월-연도" 순서로 바꿔 출력해보자.

Life = input().split(".")
print(Life[2], Life[1], Life[0], sep="-")

#다른 방법
y, m, d = input().split('.')
print(d,m,y,sep='-')