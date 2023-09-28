num1 = 10
num2 = 100

numResult = True if num1 > num2 else False
print('num1 > num2 : {}'.format(numResult))

print('num1은 num2보다 크다.') if numResult else print('num1은 num2보다 크지 않다.')

# 실습1
limitSnowAmount = 30
snowAmount = int(input('적설량 입력 (mm): '))
print(f'적설량: {snowAmount}mm, 대설경보!') if snowAmount >= limitSnowAmount else print(f'적설량: {snowAmount}mm, 대설경보 해제')

# 실습2
korScore = int(input('국어 점수 입력: '))
engScore = int(input('영어 점수 입력: '))
matScore = int(input('수학 점수 입력: '))

limitScore1 = 60
limitScore2 = 70

totalScore = korScore + engScore + matScore
totalAvgScore = totalScore / 3

print('국어: PASS') if korScore > limitScore1 else print('국어: FAIL')
print('영어: PASS') if engScore > limitScore1 else print('영어: FAIL')
print('수학: PASS') if matScore > limitScore1 else print('수학: FAIL')
print('시험: PASS') if totalAvgScore > limitScore2 else print('시험: FAIL')
print('총점: %d, 평균: %.2f' % (totalScore, totalAvgScore))




