flag = True
num = 0
sum = 0

while flag:
    num += 1
    sum += num
    print('{}까지의 합 : {}'.format(num, sum))

    if sum >= 1000:
        flag = False

# 실습1
import random

sum = 0
date = 0
flag = True

while flag:
    patientCnt = random.randint(50, 100)
    sum += patientCnt
    date += 1
    print('날짜: {}, \t 오늘 환자 수 : {}, \t 누적 환자수 : {}'.format(date, patientCnt, sum))

    if sum >= 10000:
        flag = False