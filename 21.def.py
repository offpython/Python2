def addCal():
    n1 = int(input('n1 입력 : '))
    n2 = int(input('n2 입력 : '))
    print(f'n1 + n2 = {n1 + n2}')

def printWeatherInfo():
    print('오늘 날씨는 맑습니다. 기온은 25도 입니다.')

def calFun():
    n1 = int(input('n1 입력 : '))
    n2 = int(input('n2 입력 : '))
    print(f'n1 * n1 = {n1 * n2}')
    print(f'n1 / n1 = {round(n1 / n2, 2)}')

def fun1():
    print('fun1 호출')
    fun2()
    print('fun2 호출 후에 실행!')
def fun2():
    print('fun2 호출')
    fun3()
def fun3():
    print('fun3 호출')

def printTodayWeather():
    pass

def gugudan2():
    for i in range(1, 10):
        print(f'2 * {i} = {i * 2}')
    gugudan3()
def gugudan3():
    for i in range(1, 10):
        print(f'3 * {i} = {i * 3}')
    gugudan5()
def gugudan5():
    for i in range(1, 10):
        print(f'5 * {i} = {i * 5}')

def greet(customer1, customer2):
    print(f'{customer1}, {customer2}님, 안녕하세요.')

def calculator(n1, n2):
    print(f'{n1} + {n2} = {n1 + n2}')
    print(f'{n1} - {n2} = {n1 - n2}')
    print(f'{n1} * {n2} = {n1 * n2}')
    print(f'{n1} / {n2} = {n1 / n2}')

def printNumber(*numbers):
    for number in numbers:
        print(number, end='')
    print()


def printScore(kor, eng, mat):
    sum = kor + eng + mat
    avg = sum / 3

    print(f'총점 : {sum}')
    print(f'평균 : {round(avg, 2)}')

# korScore = int(input('국어 점수 입력 : '))
# engScore = int(input('영어 점수 입력 : '))
# matScore = int(input('수학 점수 입력 : '))
# printScore(korScore, engScore, matScore)
