print('계절: 봄, 여름, 가을, 겨울')
selectStr = input('계절 입력: ')

if selectStr == '봄':
    print(f'{selectStr} is Spring')
elif selectStr == '여름':
    print(f'{selectStr} is Summer')
elif selectStr == '가을':
    print(f'{selectStr} is Fall')
elif selectStr == '겨울':
    print(f'{selectStr} is Winter')
else:
    print('목록에 없습니다.')

# 실습2
print('1.카페라떼(3.5) \t 2.에스프레소(3.0) \t 3.아메리카노(2.0) \t 4.곡물라떼(4.0) \t 5.밀크티(4.3)')
userSelectNum = int(input('메뉴 선택: '))
print('-'*20)
if userSelectNum == 1:
    print('메뉴: 카페라떼 \n가격: 3,500')
elif userSelectNum == 2:
    print('메뉴: 에스프레소 \n가격: 3,000')
elif userSelectNum == 3:
    print('메뉴: 아메리카노 \n가격: 2,000')
elif userSelectNum == 4:
    print('메뉴: 곡물라떼 \n가격: 4,000')
elif userSelectNum == 5:
    print('메뉴: 밀크티 \n가격: 4,300')
else:
    print('no menu in the list')
print('-'*20)
