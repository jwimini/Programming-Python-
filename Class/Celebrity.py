class Celebrity: # 객체를 만드는 틀이 클래스
    def __init__(self, name): # 생성자 , 초기화 하는 역할
        #이름
        self.name = name
        #소속사
        #group


    def set_name(self, name):
        self.name = name

    def set_entertainment(self, entertainment):
        self.entertainment = entertainment

    # def info(self):
    #     print(f'이름: {self.name}\t소속사 : {self.entertainment}')

    def __str__(self): # 문자열로 출력, 자동적으로 출력해줌
        return f'이름: {self.name}\t소속사 : {self.entertainment}' # <__main____. Celebrity ~~~> 나옴


class Talent(Celebrity):
    def __init__(self, name):
        super().__init__(name)            # Celebrity 클래스(부모클래스)의 생성자 호출

    def set_drama(self,drama):
        self.drama = drama

    def __str__(self):
        return super().__str__() + f'\t드라마: {self.drama}'
        # return f'이름 : {self.name} \t소속사: {self.entertainment}\t드라마: {self.drama}'

class Singer(Celebrity):
    def __init__(self, name, song):
        super().__init__(name)    # self.name = name
        self.song = song

    def __str__(self): # 문자열로 변환
        return super().__str__() + f'\t노래: {self.song}'

BH = Celebrity('변백현')          #new celebrity() in java
# BH.set_name('변백현')
BH.set_entertainment('SM')
# BH.info()
# print(BH.name, BH.entertainment)
print(BH)         #클래스의 __str__() 함수 호출됨

SH = Celebrity('오세훈')          #new celebrity() in java
# BH.set_name('변백현')
SH.set_entertainment('SM')
# SH.info()

이동욱 = Talent('이동욱')
이동욱.set_entertainment('스타쉽')
이동욱.set_drama('구미호뎐')
print(이동욱)

필릭스 = Singer('필릭스', '빽도어')
필릭스.set_entertainment('JYP')
print(필릭스)

스키즈 =[]
스키즈.append(필릭스)
print(스키즈)

for 멤버 in 스키즈:
    print(스키즈[멤버])
#
# for i in range(len(스키즈)):
#     print(스키즈[i])