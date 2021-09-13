from baseball_game_engine import make_answer, check
from custom_error import InvalidLengthError

answer = make_answer()

while True:
    guess = input("뭘까?")

    try:
        guess_int = int(guess)
    except ValueError as e:
        print('숫자를 입력하세요')
        continue
    if len(guess) != len(answer):
        raise InvalidLengthError('정답의 길이와 다른 것을 입력함')
    strike, ball = check(guess, answer)
    print(f'{guess}\tstrike: {strike}, ball: {ball}')
    if answer == guess:
        print("정답입니다.")
        break
