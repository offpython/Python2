# 백신 접종 여부 출력
age = int(input('나이 입력 : '))
vaccine = (age < 20 ) or (age >= 65)
print('age : {}, vaccine : {}'.format(age, vaccine))

# 과목별 과락 여부 출력
passScore1 = 60
passScore2 = 70

korScore = int(input('국어 점수 : '))
engScore = int(input('영어 점수 : '))
matScore = int(input('수학 점수 : '))

avgScore = (korScore + engScore + matScore) / 3
avgScoreResult = avgScore >= passScore2

korReuslt = korScore >= passScore1
engReuslt = korScore >= passScore1
matReuslt = korScore >= passScore1

subjectReuslt = korReuslt and engReuslt and matReuslt

print('평균 : {}, 결과 : {}'.format(avgScore, avgScore >= avgScoreResult))

print('국어 : {}, 결과 : {}'.format(korScore, korScore >= subjectReuslt))
print('영어 : {}, 결과 : {}'.format(engScore, engScore >= subjectReuslt))
print('수학 : {}, 결과 : {}'.format(matScore, matScore >= subjectReuslt))

print('과락 결과 : {}'.format(subjectReuslt))
print('최종 결과 : {}'.format(avgScoreResult and subjectReuslt))





