# 실습1
seletNum = int(input('출퇴근 대상자 인가요? 1.Yes \t 2.No\n답변 : '))

if seletNum == 1:
    print('교통 수단을 입력하세요.')
    trans = int(input('1.도보, 자전거 \t 2.버스, 지하철 \t 3.자가용\n입력 : '))
    if trans == 1:
        print('세금 감면 : 5%')
    elif trans == 2:
        print('세금 감면 : 3%')
    elif trans == 3:
        print('세금 감면 : 1%')
    else:
        print('잘못 입력했습니다.')
elif seletNum == 2:
    print('세금 변동 없음 ')
else:
    print('잘못 입력했습니다.')