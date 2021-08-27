import random


class Constellation:
    def __init__(self):
        self.privacy_birth = ''
        self.privacy_name = ''
        self.impormation = dict()
        self.blank = "\n\n\n\n\n"
        self.fp = "\n\n\n\n\n\t\t\t\t\t\t*******************************************************************************************************************************************\n\n\n\n\n "
        self.bb = "\n\n\n\n\n\t\t\t\t\t\t*******************************************************************************************************************************************\n\n\n\n\n"
        self.tab = '\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t'

    def show_menu(self):
        self.privacy_birth = input("본인의 생년월일을 6자리 입력하세요 (예>040411) : ")
        if len(self.privacy_birth) != 6:
            print('다시 입력하세요')
            self.show_menu()
        self.privacy_name = input("이름을 입력하세요 : ")
        if len(self.privacy_name) == 0:
            print('이름을 올바르게 입력하세요.')
            self.show_menu()

        if self.privacy_name in self.impormation.keys():
            if self.privacy_birth in self.impormation.values():
                print("\n\n\n하루에 한 번만 가능합니다 !")
                exit()

        self.impormation[self.privacy_name] = self.privacy_birth
        self.set_constellaion()

    def set_constellaion(self):

        print("\n\n\n\n ------⭐ 별자리 확인표 ⭐------")
        print("1. 물병자리 ( 1/20 ~ 2/18 )")
        print("2. 물고기자리 ( 2/19 ~ 3/20 )")
        print("3. 양자리 ( 3/21 ~ 4/19 )")
        print("4. 황소자리 ( 4/20 ~ 5/20 )")
        print("5. 쌍둥이자리 ( 5/21 ~ 6/21 )")
        print("6. 게자리 ( 6/22 ~ 7/22 )")
        print("7. 사자자리 ( 7/23 ~ 8/22 )")
        print("8. 처녀자리 ( 8/23 ~ 9/23 )")
        print("9. 천칭자리 ( 9/24 ~ 10/22 )")
        print("10. 전갈자리 ( 10/23 ~ 11/22 )")
        print("11. 사수자리 ( 11/23 ~ 12/24 )")
        print("12. 염소자리 ( 12/25 ~ 1/19 )")
        number = input("당신의 별자리 숫자를 입력하시오: ")

        if number == '1':
            self.Aquarius()
        elif number == '2':
            self.Pisces()
        elif number == '3':
            self.Aries()
        elif number == '4':
            self.Taurus()
        elif number == '5':
            self.Gemini()
        elif number == '6':
            self.Cancer()
        elif number == '7':
            self.Leo()
        elif number == '8':
            self.Virgo()
        elif number == '9':
            self.Libra()
        elif number == '10':
            self.Scorpio()
        elif number == '11':
            self.Sagittarius()
        elif number == '12':
            self.Capricorn()

    def Aquarius(self):  # 물병자리
        print(f'{self.blank}{self.fp}{self.tab}{self.privacy_name}님의 결과는 ...?')
        input(f'{self.tab}엔터를 쳐주세요 !{self.fp}{self.blank}')
        text = random.randint(1, 4)
        if text == 1:
            print(f"{self.blank}{self.fp}{self.tab}공격적인 태도로 운을 높이세요😊❗ \n"
                  f"{self.tab}자신에게 긍정적으로 말하기!!!{self.bb}")
        elif text == 2:
            print(f"{self.blank}{self.fp}{self.tab}쓸때 없는 소문으로 혼동 될 수 있습니다\n"
                  f"{self.tab}눈앞에있는 것에 신경 쓰지 말고 집중하세요☺{self.bb}")
        else:
            print(f"{self.blank}{self.fp}{self.tab}오늘은 다른사람들과 좋은 관계를 맺을 수있는 날이에요!! \n"
                  f"{self.tab}무표정보다는 미소를 지으며 상대에게 말을 걸어보는건 어떨까요?😆{self.bb}")

    def Pisces(self):  # 물고기자리
        print(f'{self.blank}{self.fp}{self.tab}{self.privacy_name}님의 결과는 ...?')
        input(f'{self.tab}엔터를 쳐주세요 !{self.fp}{self.blank}')
        text = random.randint(1, 4)
        if text == 1:
            print(f"{self.blank}{self.fp}{self.tab}오늘은 쇼핑하면 지난번부터 정말 사고 싶은것을 살 수 있을꺼 같은데요?!?!쇼핑운이 엄청나요 ♪\n"
                  f"{self.tab}그리고 오늘은 정말 기분좋은 하루를 보낼수 있을 꺼 같아요💛💛{self.bb}")
        elif text == 2:
            print(f"{self.blank}{self.fp}{self.tab}오늘은 좀,, 말 하나하나를 신중하게해야해요😫,, 문제가 생길수도 있습니다,,\n"
                  f"{self.tab}뭔가 문제가 있다면 가족과 얘기 해보는게 어떨까요? 대화에서 문제해결에 대한 힌트가 있을 수 있습니다{self.bb}")
        else:
            print(f"{self.blank}{self.fp}{self.tab}으,,, 엄청 스트레스를 많이 받으셨구나ㅜ\n"
                  f"{self.tab}진지한 감정이나 분위기에서 벗어나 재미있는 일을하면서 시간을 보내면서 스트레스를 해소해 보아요!{self.bb}")

    def Aries(self):  # 양자리
        print(f'{self.blank}{self.fp}{self.tab}{self.privacy_name}님의 결과는 ...?')
        input(f'{self.tab}엔터를 쳐주세요 !{self.fp}{self.blank}')
        text = random.randint(1, 4)
        if text == 1:
            print(f"{self.blank}{self.fp}{self.tab}오늘은 융통성있게 행동한다면 약점이나 어려운점을 극복할 수 있을겁니다!{self.bb}")
        elif text == 2:
            print(f"{self.blank}{self.fp}{self.tab}오늘은 나 자신을 돌아보는 하루가 될거 같아요\n"
                  f"{self.tab}또 자신을 돌아보면서 내가 미래에 갈 길을 생각하게 되는 계기가 될거 같아요🙃{self.bb}")
        else:
            print(f"{self.blank}{self.fp}{self.tab}오늘은 무엇이든 망설이지 말고 자신을 어필하는게 좋을꺼 같아요!\n"
                  f"{self.tab}더 매력적이고 인기쟁이가 될 수 있을꺼 같아요{self.bb}")

    def Taurus(self):  # 황소자리
        print(f'{self.blank}{self.fp}{self.tab}{self.privacy_name}님의 결과는 ...?')
        input(f'{self.tab}엔터를 쳐주세요 !{self.fp}{self.blank}')
        text = random.randint(1, 4)
        if text == 1:
            print(
                f"{self.blank}{self.fp}{self.tab}오늘은 모든 일을 다 했다고 해서 제출하거나 완벽하게 생각하지말고 끝까지 남은 부분을 수정하고 검토하는게 좋을꺼 같아요🤗{self.bb}")
        elif text == 2:
            print(f"{self.blank}{self.fp}{self.tab}오늘은 주변에서 당신에게 관심이 모이는 날! 긍정적인 말을 할 수록 더 많은 관심이 모여요😁{self.bb}")
        else:
            print(f"{self.blank}{self.fp}{self.tab}오늘은 소심하게 행동하기 보단 조금 대담하게 행동 하기! \n"
                  f"{self.tab}그러면 좋은 결과가 있을 수도,,?{self.bb}")

    def Gemini(self):  # 쌍둥이자리
        print(f'{self.blank}{self.fp}{self.tab}{self.privacy_name}님의 결과는 ...?')
        input(f'{self.tab}엔터를 쳐주세요 !{self.fp}{self.blank}')
        text = random.randint(1, 4)
        if text == 1:
            print(f"{self.blank}{self.fp}{self.tab}오늘은 내 생각을 밀어 붙이기 보단 다른 사람의 말을 더 귀 기울여 듣는것이 좋을꺼 같아요!{self.bb}")
        elif text == 2:
            print(f"{self.blank}{self.fp}{self.tab}오늘 하는 일 모든일에 속도가 빨라지는날!\n"
                  f"{self.tab}시간을 좀 더 효율적으로 쓸수 있고 작업의 속도가 빨라서 어쩌면 빨리 퇴근 할 수 있을지도..?{self.bb}")
        else:
            print(f"{self.blank}{self.fp}{self.tab}오! 오늘같은 날엔 공모전 같은 대회에 출전하는게 좋겠어요! \n"
                  f"{self.tab}예선에 붙을수도 있다는 그런 기운이 느껴져요{self.bb}")

    def Cancer(self):  # 게자리
        print(f'{self.blank}{self.fp}{self.tab}{self.privacy_name}님의 결과는 ...?')
        input(f'{self.tab}엔터를 쳐주세요 !{self.fp}{self.blank}')
        text = random.randint(1, 4)
        if text == 1:
            print(f"{self.blank}{self.fp}{self.tab}오늘은 유용한 정보를 SNS 확인하면서 얻는건 어떨까요?\n"
                  f"{self.tab}완전 괜찮은 정보를 얻을지도 몰라요!{self.bb}")

        elif text == 2:
            print(f"{self.blank}{self.fp}{self.tab}오늘은 새로운 시도에 겁먹지말고 도전하세요! \n"
                  f"{self.tab}남들이 뭐라고 하던 새로운 시도에 두려워하지 마세요! 좋은결과가 있을껍니다💕{self.bb}")
        else:
            print(f"{self.blank}{self.fp}{self.tab}오늘 하루는 일과 공부에 많은 시간을 투자하는건 어떨까요? \n"
                  f"{self.tab}좋은 성과를 얻을 수 있을꺼 같아요❣{self.bb}")

    def Leo(self):  # 사자자리
        print(f'{self.blank}{self.fp}{self.tab}{self.privacy_name}님의 결과는 ...?')
        input(f'{self.tab}엔터를 쳐주세요 !{self.fp}{self.blank}')
        text = random.randint(1, 4)
        if text == 1:
            print(f"{self.blank}{self.fp}{self.tab}오늘은 일, 공부 보다 취미와 레슨에 집중해보세요!\n"
                  f"{self.tab}나를 좀 더 향상시키자구요!{self.bb}")
        elif text == 2:
            print(f"{self.blank}{self.fp}{self.tab}곧 큰 일이 다가올꺼 같아요\n"
                  f"{self.tab}그 일을 시도하는것을 두려워하지말고 꼭 도전하세요❕❕{self.bb}")
        else:
            print(f"{self.blank}{self.fp}{self.tab}오늘은 많은 사람들을 만나게 될꺼같아요 \n"
                  f"{self.tab}새로운 사람들도 만나고 내 일과 관련된 사람들도 만날수 있으니 명함을 꼭 챙기세요❕❕{self.bb}")

    def Virgo(self):  # 처녀자리
        print(f'{self.blank}{self.fp}{self.tab}{self.privacy_name}님의 결과는 ...?')
        input(f'{self.tab}엔터를 쳐주세요 !{self.fp}{self.blank}')
        text = random.randint(1, 4)
        if text == 1:
            print(f"{self.blank}{self.fp}{self.tab}오늘은 작은 실수를 할 수도 있을꺼 같아요\n"
                  f"{self.tab}실수를 방지하기 위해 제출할 과제,서류 등 해야할 일을 잘 확인하세요!{self.bb}")
        elif text == 2:
            print(f"{self.blank}{self.fp}{self.tab}오늘은 가족들의 따스함으로 인해 감사함을 느낄수 있는 하루가 될꺼같아요🥰🥰{self.bb}")
        else:
            print(f"{self.blank}{self.fp}{self.tab}오늘은 내가 정말 친해지고 싶은 친구가 있다면 주저하지 말고 말을 거세요!!!\n"
                  f"{self.blank}{self.fp}{self.tab}부끄러워하지 않고 말을 하다보면 좋은 사람이라는 것을 알게 될꺼에요!{self.bb}")

    def Libra(self):  # 천칭자리
        print(f'{self.blank}{self.fp}{self.tab}{self.privacy_name}님의 결과는 ...?')
        input(f'{self.tab}엔터를 쳐주세요 !{self.fp}{self.blank}')
        text = random.randint(1, 4)
        if text == 1:
            print(f"{self.blank}{self.fp}{self.tab}오늘은 주변에 힘들어 하거나 도움을 필요로 하는 사람이 있다면 조언을 해주세요!\n"
                  f"{self.tab}그 사람에게 좋은 조언을 해줄수 있을 꺼 같아요!{self.bb}")
        elif text == 2:
            print(f"{self.blank}{self.fp}{self.tab}오늘은 주변에 있는 사람들이 당신을 도와주려고 할거에요! 그땐 주저하지말고 도움받기!{self.bb}")
        else:
            print(f"{self.blank}{self.fp}{self.tab}오늘은 예상하지 못했던 부분에서 좋은 기회가 올 것입니다!\n"
                  f"{self.tab}그 기회를 놓치지 말고 꼭 잡으세요! 그 기회가 뭐든 주변 사람들 모두 당신의 편이라는 것도 잊지 않기!{self.bb}")

    def Scorpio(self):  # 전갈자리
        print(f'{self.blank}{self.fp}{self.tab}{self.privacy_name}님의 결과는 ...?')
        input(f'{self.tab}엔터를 쳐주세요 !{self.fp}{self.blank}')
        text = random.randint(1, 4)
        if text == 1:
            print(f"{self.blank}{self.fp}{self.tab}오늘은 충동적인 구매가 많을꺼 같아요\n"
                  f"{self.tab}쇼핑을 간다면 목록을 적어서 딱 필요한 것만 살수 있도록 준비하세요!{self.bb}")
        elif text == 2:
            print(f"{self.blank}{self.fp}{self.tab}오늘은 용기가 가득가득한 날이에요! \n"
                  f"{self.tab}막 화가 나는데 말을 못하고 있었다면 오늘 딱! 용기내서 시원하게 한 마디 하기!{self.bb}")
        else:
            print(f"{self.blank}{self.fp}{self.tab}오늘은 전부터 받고 있던 압박감으로 인해 기분은 별로 좋지 않네요ㅜㅜ\n"
                  f"{self.tab}하던 일은 다 미뤄놓고 오늘 하루는 친구들과 맛있는것도 먹고 신나게 놀면서 리프레쉬하자구요~{self.bb}")

    def Sagittarius(self):  # 궁수자리
        print(f'{self.blank}{self.fp}{self.tab}{self.privacy_name}님의 결과는 ...?')
        input(f'{self.tab}엔터를 쳐주세요 !{self.fp}{self.blank}')
        text = random.randint(1, 4)
        if text == 1:
            print(f"{self.blank}{self.fp}{self.tab}오늘은 매번 했던거, 맨날 가던곳 이렇게 익숙한 곳 말고 새롭게 활동의 폭을 넓혀보면 어떨까요?{self.bb}")
        elif text == 2:
            print(f"{self.blank}{self.fp}{self.tab}오늘은 활기차게 좋은 하루를 보낼수 있을꺼 같아요!{self.bb}")
        else:
            print(f"{self.blank}{self.fp}{self.tab}오늘은 좋은 사람을 만날꺼 같아요! 장소가 어디든 정말 좋은 사람을 만날꺼 같아요!{self.bb}")

    def Capricorn(self):  # 염소자리
        print(f'{self.blank}{self.fp}{self.tab}{self.privacy_name}님의 결과는 ...?')
        input(f'{self.tab}엔터를 쳐주세요 !{self.fp}{self.blank}')
        text = random.randint(1, 4)
        if text == 1:
            print(f"{self.blank}{self.fp}{self.tab}오늘은 일 또는 공부로 인해 스트레스가 증가하네요😢😢 \n"
                  f"{self.tab}중간중간 틈틈히 쉬면서 스트레스를 조금씩 해소해요ㅜㅜ{self.bb}")
        elif text == 2:
            print(f"{self.blank}{self.fp}{self.tab}오늘은 원하는 것을 얻을수 있는 날! \n"
                  f"럭키 데이~!!!!!!!!!!!!!{self.bb}")
        else:
            print(f"{self.blank}{self.fp}{self.tab}오늘은 직감과 움직임을 믿어보세요!\n"
                  f"{self.tab}그 직감 뒤에 행복한 이벤트가 숨겨져 있을꺼에요😍😍{self.bb}")

    def __str__(self):
        pass
