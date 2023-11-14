num = 0

while True:
    print('hello ~~ ')

    num += 1
    if num >= 5:
        break

print('The End')

sum = 0
searchNum = 0

for i in range(100):
    sum += i

    if sum > 100:
        searchNum = i
        break

print('searchNum : {}'.format(searchNum))

# 실습1

result = 1
num = 0

for i in range(1, 11):
    result *= i

    if result > 50:
        num = i
        break

print('num : {}, result: {}'.format(num, result))

# 실습2
limitWeight = 2200
currentWeight = 800
date = 1

while True:
    if currentWeight >= limitWeight:
        break

    date += 1
    currentWeight += 70

print('이유식 중단 날짜: {}'.format(date))