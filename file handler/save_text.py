f = open('text.txt', 'w', encoding='utf-8')

f.write('지민:')
f.write('연노랑')
f.write('\n')   # 문단 내려가기
f.write('지민:')
f.write('핑크색')


with open('text.txt','w', encoding='utf-8') as f:   # close가 필요없음 자동으로 닫아줌
    f.write('지민:')
    f.write('연노랑')
    f.write('\n')  # 문단 내려가기
    f.write('지민:')
    f.write('핑크색')