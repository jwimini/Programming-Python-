from tictactoe_gameengine import TictactoeGameEngine


class TictactoeConsole:
    def __init__(self):
        self.game_engine = TictactoeGameEngine()

    def play(self):
        # show board
        self.game_engine.show_board()
        # 무한반복
        while True:
            #  input row, col
            row = int(input('행: '))
            col = int(input('열: '))            #  set row, col
            self.game_engine.set(row, col)

            #  show board
            self.game_engine.show_board()

            #  set winner
            winner = self.game_engine.set_winner()      # winner에 들어갈 수 있는 문자열 3개 : o x 무승부(d)

            #  승자가 있거나 무승부면, 게임 오버, 결과 출력
            # if winner == 'X' or 'O': 틀림(무조건 true가 된다)
            if winner == 'X' or winner == 'O':
                print(f'{winner} 이김~!~!!~!~!~🤩🤩🤩🤩🤩🤩🤩🤩🤩🤩🎉🎉🎉🎉')
                break
            elif winner == 'd':
                print('무승부 입니더~!~!🤗🤗🤗🤗🤗🤗🤗🤗🤗🤗🤗🤗')
                break

            #  change turn
            self.game_engine.change_turn()

if __name__ == '__main__':
    ttt_console = TictactoeConsole()
    ttt_console.play()
