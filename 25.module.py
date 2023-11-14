# import calculator as cal
# cal.add(10, 20)
# cal.div(10, 20)
# cal.mul(10, 20)
# cal.sub(10, 20)

# from calculator import add
# from calculator import sub
# from calculator import mul
# from calculator import div

# from calculator import *

from calculator import add, mul
add(10, 20)
# sub(10, 20)
mul(10, 20)
# div(10, 20)

import scores as s

korScore = int(input('국어 점수 입력 : '))
engScore = int(input('영어 점수 입력 : '))
matScore = int(input('수학 점수 입력 : '))

s.addScore(korScore)
s.addScore(engScore)
s.addScore(matScore)

print(f'과목 점수 : {s.getScore()}')
print(f'총점 : {s.getTotalScore()}')
print(f'평균 : {round(s.getAvgScore(), 2)}')




