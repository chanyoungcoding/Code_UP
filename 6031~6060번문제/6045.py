#6045문제
#정수 3개를 입력받아 합과 평균을 출력해보자

a,b,c = input().split()
avg = (int(a) + int(b) + int(c))
print(avg, "%.2f" % (avg/3))



