userName = 'Hong gil dong'
userAge = 21

print("user name : {}".format(userName))
print("user age : {}".format(userAge))
print('user name : {}, user age : {}'.format(userName, userAge))
print(f'user name : {userName}, user age : {userAge}')

print('ㄴㅏ의 이름은 {0}이고, 나이는 {1}살 입니다. {0}이름은 아버님께서 지어 주셨습니다.'.format(userName, userAge))

# 형식 문자를 이용한 데이터 출력
# %s : 문자열, %d : 정수, %f: 실수
print("user name : %s" % userName)
print("user age : %d" % userAge)
print(f'user name : %s, user age : %d' % (userName, userAge))

pi = 3.14
print('pi :%f' % pi)
print('pi :%.2f' % pi)
print('pi :%.d' % pi)

