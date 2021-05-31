class Drink:
    _CUPS = ('레귤러', '점보')
    _ICES = ('0%', '50%', '100%', '150%')  # 100%
    _SUGARS = ('0%', '50%', '100%', '150%')  # 100%

    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.cup = 0  # '레귤러' Drink._CUPS[self.cup]
        self.ice = 2  # '100%' Drink._ICES[self.ice]
        self.sugar = 2  # ' 100%'

    def set_cup(self):
        for index, cup in enumerate(Drink._CUPS):
            print(f'{index + 1}: {cup}')  # 컵 종류 보여주기

        cup = input('컵사이즈를 선택하세요: ')  # 컵 선택하기
        if cup == '':
            self.cup = 0
        else:
            cup = int(cup)
            self.cup = cup - 1  # 컵 self 에 넣기

        if self.cup == 1:  # 점보일때 +500
            self.price += 500

    def set_ice(self):
        for index, ice in enumerate(Drink._ICES):  # 얼음량 종류 보여주기
            print(f'{index + 1}: {ice}')
        ice = input('얼음량을 선택하세요: ')  # 선택하기
        # if ice =='':
        #     self.ice = 2
        # else:
        #     self.ice = int(ice) - 1
        self.ice = 2 if ice == '' else int(ice) - 1  # self.ice 에 설정하기

    def set_sugar(self):
        for index, sugar in enumerate(Drink._SUGARS):  # 당도 종류 보여주기
            print(f'{index + 1}: {sugar}')
        sugar = input('당도를 선택하세요: ')  # 당도 선택하기
        self.sugar = 2 if sugar == '' else int(sugar) - 1  # self.sugar 에 넣기

    def order(self):
        self.set_cup()
        self.set_ice()
        self.set_sugar()

    def __str__(self):
        return f'이름: {self.name}\t가격: {self.price}\t컵사이즈: {Drink._CUPS[self.cup]}\t얼음양: {Drink._ICES[self.ice]}\t당도: {Drink._SUGARS[self.sugar]}'


class Coffee(Drink):
    pass


class Bubbletea(Drink):
    _PEARLS = ('타피오카', '화이트', '알로에', '젤리')

    def __init__(self, name, price):
        super().__init__(name, price)  # 부모초기화 호출
        self.pearls = 0  # '타피오카'

    def set_pearl(self):
        for index, pearl in enumerate(Bubbletea._PEARLS):  # 펄 종류 보여주자
            print(f'{index + 1}: {pearl}')
        pearl = input('펄을 골라주세요: ')  # 펄 선택하자
        self.pearl = 0 if pearl == '' else int(pearl) - 1  # self.pearl에 넣자

    def order(self):
        super().order()  # 부모 클래스의 order() 호출하기
        self.set_pearl()  # set_pearl() 호출하기

    def __str__(self):
        result = super().__str__()  # 부모클래스의 __str__()(이름, 가격, 컵사이즈, 얼음량, 당도), 펄
        return result + f'\t펄종류: {Bubbletea._PEARLS[self.pearl]}'


class Order:
    def __init__(self):
        self.menu = []  # self.menu 매장에 잇는 음료수 전체
        self.init_menu()  # init.menu()
        self.order_menu = []  # self.order_menu 내가 고른 메뉴들

    def init_menu(self):
        지민늬꺼 = Coffee('아캬마', 2500)
        세훈이꺼 = Bubbletea('초콜릿밀크티', 3900)
        백현이꺼 = Bubbletea('연한아메리카노', 3400)
        self.menu.append(지민늬꺼)
        self.menu.append(세훈이꺼)
        self.menu.append(백현이꺼)

    def show_menu(self):
        for index, drink in enumerate(self.menu):
            print(f'{index + 1}: {drink.name}\t{drink.price}원')

    def sum_price(self):
        sum_value = 0#self.order_menu 하나씩 꺼내서 drink 의 가격을 합산 하고 리턴
        for drink in self.order_menu:
            sum_value += drink.price
        return sum_value

    def order_drink(self):
        while True:  # 반복
            self.show_menu()  # 메뉴 보여주기
            drink = input('메뉴를 선택하세요: ')  # 메뉴 선택하기
            drink = int(drink) - 1
            new_drink = self.menu[drink]
            new_drink.order()  # 옵션 선택하기
            self.order_menu.append(new_drink)  # self.order.menu 에 추가하기
            is_add = input('더 주문하시겠습니까?(n:은 종료)')  # 더 주문할껀가?
            if is_add == 'n':
                break
        print(self)  # 주문 내역 보여주기

    def __str__(self):
        s = '-' * 20 + '주문 내역' + '-' * 20+ '\n'
        # 주문내역 제목 보여주기
        for drink in self.order_menu:  # 주문한 음료수들 목록 보여주기
            s += str(drink) + '\n'
        s += f'총 금액: {self.sum_price()}원'  # 총 합계 가격 보여주기
        return s


# 지뮈니꺼 = Bubbletea('카페모카', 2500)
# 지뮈니꺼.order()
# print(지뮈니꺼)
order = Order()
order.order_drink()
