# 횟수에 의한 반복 (for문)

for i in range(1, 10):
    result = 7 * i
    print('{} * {} = {}'.format(7, i, result))

for k in range(100):
    pass

for h in range(5):
    print('Hi', end='')
    print(' loop statement')

for num in range(5):
    print('Hello Python')

gugudanNum = int(input('구구단: '))
for num in range(1, 10):
    result = gugudanNum * num
    print('{} * {} = {}'.format(gugudanNum, num, result))

startNum = int(input('반복의 시작 입력 : '))
endNum = int(input('반복의 끝 입력 : '))

for i in range(startNum, endNum + 1, 2):
    print(i)
