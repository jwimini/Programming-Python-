print('전체 한꺼번에 읽기')
f = open('text.txt', 'r', encoding='utf-8')

data = f.read()

f.close()

print(data)

print('한 줄씩 읽기')
f = open('text.txt', 'r', encoding='utf-8')
while True:
    line = f.readline()     # line: wlalsd연노랑\n
    if line == '':        # 파일 빈칸 이라면 끝내기
        break
    print(line.rstrip())    # line.replace('\n', '')

f.close()

print('전체를 한꺼번에 읽고, 줄 별로 리스트')
f = open('text.txt', 'r', encoding='utf-8')
lines = f.readlines()
f.close()
for line in lines:
    print(line.rstrip())

#Quiz
# 이름: wlalsdl[tab]좋아하는 색: 연노랑
# 이름: 지민[tab]좋아하는 색: 연노랑
print('지민[tab]좋아하는 색: 연노랑')
f = open('text.txt', 'r', encoding='utf-8')
lines = f.readlines()
f.close()
for line in lines:
    print('이름: ' + line.rstrip()[:3] + '\t좋아하는 색:' + line.rstrip()[-3:])
    print('이름: ' + data[0].rstrip() + '\t좋아하는 색:' + data[1].rstrip())
