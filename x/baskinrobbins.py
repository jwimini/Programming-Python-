class Icecream:
    def __init__(self, name): # 생성자. 주로 변수 초기화
        self.name = name

    def set_explanation(self, explanation):
        self.explanation = explanation
    # 이름 name
    # 설명 explanation
    def __str__(self):          # 객체를 우리가 알아보기 쉽게 문자열로 리턴, 주로 print()
        return f'이름 : {self.name}'

# 아이스홈런볼 = Icecream('아이스홈런볼')
# 아이스홈런볼.set_explanation('초콜릿 아이스크림과 바닐라 아이스크림 속에 초코코팅 홈런볼과 피넛이 쏙쏙!')
# print(아이스홈런볼)
# print(아이스홈런볼.explanation)
#
# 자모카아몬드훠지 = Icecream('자모카아몬드훠지')
# print(자모카아몬드훠지)
# 메이플월넛 = Icecream('메이플월넛')
# print(메이플월넛)
# 트리플민초 = Icecream('트리플민초')
# print(트리플민초)

class Order:
    _CATEGORIES = ('싱글레귤러', '더블레귤러', '파인트')
    _PRICES = [3200, 6200, 8200]
    def __init__(self):
        # 종류: 콘, 파인트
        self.set_cateries()
        #메뉴
        self.menu = []
        self.init_menu()
        #주문한 메뉴
        self.order_menu = []

    def __str__(self):
        pass

    def set_cateries(self):
        for index, category in enumerate(Order._CATEGORIES):
            print(index+1, category)
        category_num = input('종류를 골라주세요 : ')
        self.category = int(category_num)

    def init_menu(self):
        self.menu.append(Icecream('자모카아몬드훠지'))
        self.menu.append(Icecream('메이플월넛'))
        self.menu.append(Icecream('트리플민초'))

    def show_menu(self):
        for index, icecream in enumerate(self.menu):
            print(f'{index+1}. {icecream}')

    def order(self):
        # 아이스크림 보여주자(메뉴보여주자)
        self.show_menu()
        for _ in range(self.category):      # 종류에 따라 반복
            #   메뉴선택
            icecream = input('아이스크림을 골라주세요 :')
            icecream = int(icecream)
        #   주문한 메뉴에 추가하자
            self.order_menu.append(self.menu[icecream - 1])
        # 종류를 출력하자
        print('-'*10 + '주문 내역 입니다' + '-'*10)
        print(Order._CATEGORIES[self.category -1])
        print(str(Order._PRICES[self.category -1]) + '원')
        # 주문한 메뉴 출력하자
        for icecream in self.order_menu:
            print(icecream)

order = Order()
order.order()
