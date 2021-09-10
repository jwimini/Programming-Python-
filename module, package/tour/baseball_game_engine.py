import random


# 정답 만들고: 숫자 세개 뽑기
def make_answer(self):
    list_r = random.sample(range(9 + 1), 3)
    return "".join(map(str, list_r))


def check(guess, answer):
    strike = 0
    ball = 0
    # 숫자 하나 꺼내서 정답에 있고, 자리가 같으면, strike  += 1
    # 숫자 하나 꺼내서 정답에 있고, 자리가 다르면, ball += 1

    for i, g in enumerate(guess):
        for j, a in enumerate(answer):  # 숫자가 같으면
            if g == a:
                if i == j:
                    strike += 1
                else:
                    ball += 1

    # guess[0] == answer[0]
    # guess[0] == answer[1]
    # guess[0] == answer[2]
    # guess[1] == answer[0]
    # guess[1] == answer[1]
    # guess[1] == answer[2]
    # guess[2] == answer[0]
    # guess[2] == answer[1]
    # guess[2] == answer[2]

    return strike, ball


if __name__ != '__main__':
    answer = make_answer()
    print(answer)
    strike, ball = check("832", "934")
    print(strike, ball)  # 1 0
    strike, ball = check("431", "934")
    print(strike, ball)  # 1 1
    strike, ball = check("934", "934")
    print(strike, ball)  # 3 0
