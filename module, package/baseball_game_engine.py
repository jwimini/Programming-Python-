import random
def make_answer():
    answer = random.sample(range(0,9,1),3)
    return  "".join(str(n) for n in answer)


def check(guess, answer):
    strike = 0
    ball = 0
    #숫자 하나 꺼내서 정답에 있고, 자리가 같으면 strike += 1
    #숫자 하나 꺼내서 정답에 있고, 자리가 다르면, ball += 1
    for i, g in enumerate(guess):
        for j, a in enumerate(answer):
            if g == a:  #숫자가 같으면
                if i == j:  #자리가 같으면
                    strike += 1
                else:       #자리가 다르면
                    ball += 1
    return strike,ball


if __name__ == '__main__':

    answer = make_answer()
    print(answer)
    check()
    strike, ball = check("831","934")
    print(strike, ball)     #1 0
    strike, ball = check("431","934")
    print(strike, ball)     #1 1
    strike, ball = check("934","934")
    print(strike, ball)     #3 0