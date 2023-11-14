def calculator(n1, n2):
    result = n1 + n2
    return result

# returnValue = calculator(20, 10)
# print(f'return value : {returnValue}')

def divideNumber(n):
    if n % 2 == 0:
        return '짝수'
    else:
        return '홀수'

# returnValue =divideNumber(5)
# print(f'return value : {returnValue}')

def cmToMm(cm):
    result = cm * 10
    return result

# length = float(input('길이(cm) 입력 : '))
# returnValue = cmToMm(length)
# print(f'return value : {returnValue}mm')

import random

def getOddRandomNum():
    while True:
        rNum = random.randint(1, 100)
        if rNum % 2 != 0:
            break
    return rNum

# print(f'return value : {getOddRandomNum()}')

# num_out = 10
# def printNumbers():
#     print(f'num_out : {num_out}')
#
# printNumbers()
# print(f'num_out : {num_out}')

# num_out = 10
# def printNumbers():
#     num_out = 20
#     print(f'num_out : {num_out}')
# printNumbers()
# print(f'num_out : {num_out}')

# num_out = 10
# def printNumber():
#     global num_out
#     num_out = 20
#     print(f'num_out : {num_out}')
# printNumber()
# print(f'num_out : {num_out}')

# def printArea():
#     triangleArea = width * height / 2
#     squreArea = width * height
#     print(f'삼각형 넓이 : {triangleArea}')
#     print(f'사각형 넓이 : {squreArea}')
#
# width = int(input('가로 길이 입력 : '))
# height = int(input('세로 길이 입력 : '))
# printArea()

totalVisit = 0

def countTotalVisit():
    global totalVisit
    totalVisit += 1
    print(f'누적 방문객 : {totalVisit}')

countTotalVisit()
countTotalVisit()
countTotalVisit()
