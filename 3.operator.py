num1 = 10; num2 = 5

result = num1 > num2
print('num1 > num2 : {}'.format(result))

result = num1 >= num2
print('num1 >= num2 : {}'.format(result))

result = num1 < num2
print('num1 < num2 : {}'.format(result))

result = num1 <= num2
print('num1 <= num2 : {}'.format(result))

result = num1 == num2
print('num1 == num2 : {}'.format(result))

result = num1 != num2
print('num1 != num2 : {}'.format(result))

userInputNumber1 = int(input('첫 번째 숫자 입력 : '))
userInputNumber2 = int(input('두 번째 숫자 입력 : '))

print('{} > {} : {}'.format(userInputNumber1, userInputNumber2, (userInputNumber1 > userInputNumber2)))
print('{} >= {} : {}'.format(userInputNumber1, userInputNumber2, (userInputNumber1 >= userInputNumber2)))
print('{} < {} : {}'.format(userInputNumber1, userInputNumber2, (userInputNumber1 < userInputNumber2)))
print('{} <= {} : {}'.format(userInputNumber1, userInputNumber2, (userInputNumber1 <= userInputNumber2)))
print('{} == {} : {}'.format(userInputNumber1, userInputNumber2, (userInputNumber1 == userInputNumber2)))
print('{} != {} : {}'.format(userInputNumber1, userInputNumber2, (userInputNumber1 != userInputNumber2)))
