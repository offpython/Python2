# for문 while문 비교

sum = 0
for i in range(1, 11):
    sum += i
print('sum : {}'.format(sum))

sum = 0
n = 1
while n < 11:
    sum += n
    n += 1
print('sum : {}'.format(sum))

##
sum = 0
maxInt = 0

for i in range(1, 101):

    if i % 7 == 0 and sum <= 50:
        sum += i
        maxInt = i

    print('i : {}'.format(i))
print('7의 배수의 합이 50 이상인 최초의 정수 : {}'.format(maxInt))

sum = 0
maxInt = 0
n = 1

while n <=100 and sum <= 50:
    n += 1

    if n % 7 == 0:
        sum += n
        maxInt = n
    print('i : {}'.format(i))

print('7의 배수의 합이 50 이상인 최초의 정수 : {}'.format(maxInt))

# 실습1
currentThickness = 30
rotationCnt = 0
removeThickness = 0.15

while currentThickness >= 20:
    rotationCnt += 1
    currentThickness -= removeThickness

safeRotationCnt = rotationCnt - 1
print('운행 가능 횟수 : {}'.format(safeRotationCnt))
