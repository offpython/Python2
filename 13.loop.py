# print('{} * {} = {}'.format(2, 1, (2*1)))
# print('{} * {} = {}'.format(2, 2, (2*2)))
# print('{} * {} = {}'.format(2, 3, (2*3)))
# print('{} * {} = {}'.format(2, 4, (2*4)))
# print('{} * {} = {}'.format(2, 5, (2*5)))
for i in range(1, 10):
    print('{} * {} = {}'.format(2, i, (2 * i)))

# print('{} 선수한테 메일 발송!'.format('박지성'))
# print('{} 선수한테 메일 발송!'.format('손흥민'))
# print('{} 선수한테 메일 발송!'.format('김연아'))

players = ['박지성', '손흥민', '김연아']
for player in players:
    print(f'{player} 선수에게 메일 발송!')
