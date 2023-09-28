# 실습1
age = int(input('나이 입력: '))
seniorAge = 65

if age >= seniorAge:
    print('무료 대상 승객입니다.')
else:
    print('유료 대상 승객입니다. 돈 내고 타십쇼')

# 실습2
floatNum = float(input('소수 입력: '))

if floatNum - int(floatNum) >= 0.5:
    print('올림 : {}'.format(int(floatNum) + 1))
else:
    print('내림 : {}'.format(int(floatNum)))
