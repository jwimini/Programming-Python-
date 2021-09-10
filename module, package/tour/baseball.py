import baseball_game_engine

# 반복
while True:
    # 숫자를 묻고
    guess = input('답은 무엇일까여? ')
    # strike, ball 편집하기
    strike, ball = baseball_game_engine.check(guess, baseball_game_engine.answer)
    # 출력하기
    print(f'{guess}\strike:{strike}, ball : {ball}')

    # 정답 == 숫자 끝내기
    if baseball_game_engine.answer == guess:
        print("정답")
        break
