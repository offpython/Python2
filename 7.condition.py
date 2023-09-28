# 실습1

korScore = int(input('국어 점수 입력: '))
engScore = int(input('영어 점수 입력: '))
matScore = int(input('수학 점수 입력: '))

avgScore = (korScore + engScore + matScore) / 3
scorelimit = 90
print('평균: %.2f' % (avgScore))

if avgScore >= scorelimit:
    print('참 잘했어요~')

# 실습2
highTemperature = 28
lowTemperature = 20

innerTemperature = int(input('실내 온도 입력: '))

if innerTemperature >= 28:
    print('냉방 작동!')
elif innerTemperature <= 20:
    print('난방 작동!')