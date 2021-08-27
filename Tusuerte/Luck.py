import random
from Constellation import Constellation


class Luck:
    def __init__(self):
        self.privacy_birth=''
        self.privacy_name=''
        self.impormation = dict()
        self.blank = "\n\n\n\n\n"
        self.fp = "\n\n\n\n\n\t\t\t\t\t\t*******************************************************************************************************************************************\n\n\n\n\n "
        self.bb = "\n\n\n\n\n\t\t\t\t\t\t*******************************************************************************************************************************************\n\n\n\n\n"
        self.tab = '\t\t\t\t\t\t\t\t\t\t\t\t'

    def show_menu(self, null=None):
        self.privacy_birth = input("본인의 생년월일을 입력하세요 (예>040411) : ")
        if len(self.privacy_birth) != 6:
            print('다시 입력하세요')
            self.show_menu()
        self.privacy_name = input("이름을 입력하세요 : ")
        if len(self.privacy_name) == 0 :
            print('이름을 올바르게 입력하세요.')
            self.show_menu()

        if self.privacy_name in self.impormation.keys():
            if self.privacy_birth in self.impormation.values():
                print("\n\n\n하루에 한 번만 가능합니다 !")
                exit()

        self.impormation[self.privacy_name] = self.privacy_birth
        self.set_luck()

    def set_luck(self):
        print('1. 연애운💕')
        print('2. 시험운📝')
        print('3. 건강운💪')
        print('4. 하루운세🌈')
        print('5. 종료')
        a = input("보고싶은 운세를 선택하세요 : ")
        if a == '1':
            self.Love_Luck()
        elif a == '2':
            self.Test_Luck()
        elif a == '3':
            self.Health_Luck()
        elif a == '4':
            self.Daily_horoscope()
        elif a == '5':
            print('감사합니다.')
        else:
            print("다시 입력하세요")
            self.set_luck()

    def Love_Luck(self):
        print(f'{self.blank}{self.fp}{self.tab}\t\t\t\t\t\t\t{self.privacy_name}님의 결과는 ...?')
        input(f'{self.tab}\t\t\t\t\t\t\t엔터를 쳐주세요 !{self.fp}{self.blank}')

        r = random.randint(1, 6)
        if r == 1:
            print(f"{self.blank}{self.fp}{self.tab}솔로 - 가까운 주변에 누군가가 지켜보고 있습니다.👀\n{self.tab}" +
                  f"상대이성이 주변을 빙빙 돌며 짝사랑을 하고 있거나 연락을 하지 않고, 단절된 누군가가 sns를 염탐하며 그리워하고 있습니다.\n{self.tab}"
                  f"이후 상대이성과 거리감이 좁혀지고 서로가 만날 인연이기 때문에 예상치 못한 곳에서 좋게 마주할 수 있습니다.🥰\n\n{self.tab}"
                  f"커플 - 상대 연인이 바쁜 시기가 될 수 있습니다. 또는 상대 연인이 다른 지역으로 이사를 가는 상황이 생길 수 도있습니다.\n{self.tab}"
                  f"평소보다 데이트 횟수나 연락의 빈도수가 줄어들 수도 있습니다.😥 \n{self.tab}"
                  f"관계의 평화를 위해서 자신의 마음가짐을 편하게 갖고 여러분도 자신의 할 일에 대해 더 집중해보세요.{self.bb}")
        elif r == 2:
            print(self.tab + f"{self.blank}{self.fp}{self.tab}솔로 - 이번 달 초중반에 새로운 인연이 등장합니다.🤩\n{self.tab}"
                             f"서로가 강렬한 인상이며 첫눈에 반하여 서로 관계를 이어가고 싶지만 본인의 기대치가 낮아서 큰 기대를 하지 않을 수 있습니다.\n{self.tab}"
                             f"자신의 감정을 숨기지 않고 자신의 마음이 끌리는대로 자연스럽게 두면 좋은 결과가 찾아옵니다.\n\n{self.tab}"
                             f"커플 - 상대방과 트러블이 생길 수 있는 달입니다.😫\n{self.tab}"
                             f"마음속으로 참아왔던 감정이 크게 터지게 되지만 감정싸움이 오래가지 않을 것으로 보입니다.\n{self.tab}"
                             f"자신의 속마음을 솔직하게 전달하고 서로 이해한다면 긍적적인 한달을 보낼 수 있습니다.☺\n{self.bb}")
        elif r == 3:
            print(self.tab + f"{self.blank}{self.fp}{self.tab}솔로 - 당신의 잔잔한 일상에 누군가가 훅 하고 등장합니다.\n{self.tab}"
                             f"적어도 주변에 2명 이상의 사람이 당신에게 관심을 가질 수 있습니다.😎\n{self.tab}"
                             f"모든 가능성을 열어두고 상대에 대해 진심으로 알아가는 것이 좋습니다.\n\n{self.tab}"
                             f"커플 - 서로에게 쌓인 앙금을 풀고 진정한 화해가 되는 한달입니다.😉\n{self.tab}"
                             f"서로의 성향이 달라 그동안 사소했던 갈등들을 풀기위해 마음가짐을 변화시키고 진심 어린 대화를 나누려 노력하세요.✊{self.bb}")
        elif r == 4:
            print(self.tab + f"{self.blank}{self.fp}{self.tab}솔로 - 누군가와 서로 연락을 주고 받는 썸 타는 사이가 생길 것 입니다.❤\n{self.tab}"
                             f"하지만 이번 달은 상대와 우정 그 이상으로 발전하기는 어려워 마음표현을 하고 싶더라도 감정을 숨기는 것이 더 좋습니다.\n\n{self.tab}"
                             f"커플 -당신은 상대에게 감정적으로 의존하는 연애를 하고 있을 것입니다.🤸‍\n{self.tab}"
                             f"그래서 상대방이 기대치에 못 미칠 때 일방적으로 서운함을 느낄 것으로 보입니다.\n{self.tab}"
                             f"이번달은 나 자신을 더 사랑하는 연애를 하고 연락할 시간에 자신의 커리어에 더 집중하면 좋을 것 같습니다.🤗{self.bb}")
        elif r == 5:
            print(self.tab + f"{self.blank}{self.fp}{self.tab}솔로 - 당분간은 연애보단 내 일에 더 집중해서 돈을 좀 많이 벌어야겠다는 생각이 많으시네요.💲\n{self.tab}"
                             f"지금은 연애 보다 내 커리어가 더 중요!✨{self.tab}"
                             f"그리고 전 여친이나 전 남친으로 부터 연락이 올껀데요,, \n{self.tab}"
                             f"그냥 단순하게 안부를 물어보기 위한 연락인거 같네요.{self.bb}")

        input(f' \n\n\n\n\n{self.tab}\t\t\t\t\t\t엔터를 쳐주세요 !')

    def Test_Luck(self):
        print(f'{self.blank}{self.fp}{self.tab}\t\t\t\t\t\t\t{self.privacy_name}님의 결과는 ...?')
        input(f'{self.tab}\t\t\t\t\t\t\t엔터를 쳐주세요 !{self.fp}{self.blank}')
        r = random.randint(1, 6)
        if r == 1:
            print(f"{self.blank}{self.fp}{self.tab}꼼곰한 태도를 취할 필요가 있습니다.작은 부분도 빼놓지 말고말이지요.\n{self.tab}"
                             f"소홀히 해 두었던 부분에서 문제가 나올 것에 대비해 놓아햐 한다는 이야기 입니다.\n{self.tab}"
                             f"조금 더 힘을 내고 집중해서 문제를 푼다면 그만한 결과가 있을 것입니다.{self.bb}")
        elif r == 2:
            print(f"{self.blank}{self.fp}{self.tab}시험에 대해 너무 부담을 갖고 있는 것은 아닌지요.\n{self.tab}"
                             f"그렇기 때문에 어느 정도는 긴장을 풀고 여유를 가진다고 해서 나쁜 일은 아닐 것입니다.")
        elif r == 3:
            print(f"{self.blank}{self.fp}{self.tab}변화를 단행하세요. 슬슬 이제까지의 체제에 질릴 때가 되었습니다.\n{self.tab}"
                             f"그 동안 열심히 해온 것은 좋으나 조금씩 지치고 질려가고 있는 자신을 느끼는 날입니다.\n{self.tab}"
                             f"이런 날은 조금씩이라도 분위기 전환을 해 가면서 공부를 하는 것이 훨씬 유리합니다.{self.bb}")
        elif r == 4:
            print(f"{self.blank}{self.fp}{self.tab}공부를 했음에도 전혀 기억이 나지 않는다던가 시험 결과가 다소 기대에 미치치 못하게 될 것입니다.\n{self.tab}"
                             f"어느 정도 성과를 보려면 다른 사람 노력 이상을 해야만 합니다.{self.bb}")
        elif r == 5:
            print(f"{self.blank}{self.fp}{self.tab}살짝 들떠 있기 쉬운 하루입니다. 어느 정도는 당신 자신의 실력에 있어서도 자신이 있을 것입니다.\n{self.tab}"
                             f"하지만 너무 들뜬 나머지 바보같은 실수를 저질러 버릴 가능성이 상당히 높기 때문입니다.\n{self.tab}"
                             f"마음을 가라앉히고 시험에 임하도록 하세요.{self.bb}")

        input(f' \n\n\n\n\n{self.tab}\t\t\t\t\t\t엔터를 쳐주세요 !')

    def Health_Luck(self):
        print(f'{self.blank}{self.fp}{self.tab}\t\t\t\t\t\t\t{self.privacy_name}님의 결과는 ...?')
        input(f'{self.tab}\t\t\t\t\t\t\t엔터를 쳐주세요 !{self.fp}{self.blank}')
        r = random.randint(1, 6)
        if r == 1:
            print(f"{self.blank}{self.fp}{self.tab}무리하게 활동을 추구하기 보다는 컨디션을 잘 조절해야해요!\n{self.tab}"
                  f"조용하게 지내면서 내시을 다져야 하는날 입니다!{self.bb}")
        elif r == 2:
            print(f"{self.blank}{self.fp}{self.tab}무리하게 활동을 하기 보다는 여가를 즐기면서 여유로운 하루를 보내보세요!{self.bb}")
        elif r == 3:
            print(f"{self.blank}{self.fp}{self.tab}지구력이 부족해지고 쉽게 지치게 되는 날이에요,, {self.bb}")
        elif r == 4:
            print(f"{self.blank}{self.fp}{self.tab}모든 면에서 안정이 되는 날입니다. \n{self.tab}활동력이 증가하지만 무리수를 두지 않으니 컨디션이 매우 높은날 입니다.{self.bb}")
        elif r == 5:
            print(f"{self.blank}{self.fp}{self.tab}건강보다는 일을 챙기는 면이 많으니 일을 완수하고 나면 적절하게 휴식을 취하는게 좋을거 같네요!{self.bb}")

        input(f' \n\n\n\n\n{self.tab}\t\t\t\t\t\t엔터를 쳐주세요 !')

    def Daily_horoscope(self):
        print(f'{self.blank}{self.fp}{self.tab}\t\t\t\t\t\t\t{self.privacy_name}님의 결과는 ...?')
        input(f'{self.tab}\t\t\t\t\t\t\t엔터를 쳐주세요 !{self.fp}{self.blank}')
        r = random.randint(1, 6)
        if r == 1:
            print(f"{self.blank}{self.fp}{self.tab}오늘은 왠지 혼자 있고 싶은 기분이 들 수 있을꺼 같아요.\n{self.tab}"
                  f"하지만 혼자 있어도 외롭지 않고 좋은날!\n{self.tab}"
                  f"이런저런 생각도 잘 떠오르고 정리도 잘 되는날!\n{self.tab}"
                  f"밝은 빛을 통해서 희망도 보여요!\n{self.tab}"
                  f"오늘은 아주 총명한 하루가 될거 같아요.{self.bb}")
        elif r == 2:
            print(f"{self.blank}{self.fp}{self.tab}지금 뭔가 좀 쓸쓸한가봐요,,\n{self.tab}"
                  f"센 척 강한 척 하지만 마음은 외로운 하루... \n{self.tab}"
                  f"약한면을 보여주는 것을 너무 두려워하지마세요.\n{self.tab}"
                  f"그게 약점이 된다고 생각하면 일상이 너무 경직되어 버릴꺼에요.\n{self.tab}"
                  f"그래도 전첵적으로는 주어진 상황을 책임지면서 조금 릴렉스하면 더 좋을 것 같아요{self.bb}")
        elif r == 3:
            print(f"{self.blank}{self.fp}{self.tab}오늘은 문화생활을 하면 좋을것 같아요.\n{self.tab}"
                  f"책을 읽으면 머릿속에 샤샤삭 그림 그려지는 날이라구요!\n{self.tab}"
                  f"똑같은 영화를 봐도 남들이 못 보는 걸 포착해낼 수도 있고, 당신의 감수성을 조금이라도 더 촉촉하게 해줄것입니다!{self.bb}")
        elif r == 4:
            print(f"{self.blank}{self.fp}{self.tab}뭔가 마무리를 앞두고 있나봐요,,\n{self.tab}"
                  f"그래서 오늘이 힘든 하루였겠지요,,\n{self.tab}"
                  f"오늘까지도 열심히 달리시느라 수고 하셨고 힘들지만 하던일을 잘 끝내봐요!\n{self.tab}"
                  f"곧 좋은 날이 올껍니다~!!!{self.bb}")
        elif r == 5:
            print(f"{self.blank}{self.fp}{self.tab}오! 오늘 축하받을 일이 생길꺼 같아요~~ \n{self.tab}"
                  f"준비 하던 일이 좋은 결실을 맺나봐요😊 \n{self.tab}"
                  f"인간관계로는 연애보다는 우정의 기운이 세요!\n{self.tab}"
                  f"친구들이랑 약속 있다면 하하호호 즐거운 모임이 될 거 같군요!!{self.bb}")

        input(f' \n\n\n\n\n{self.tab}\t\t\t\t\t\t엔터를 쳐주세요 !')

    def __str__(self):
        pass