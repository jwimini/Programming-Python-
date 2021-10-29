class TictactoeGameEngine:
    def __init__(self):
        self.board = list('.' * 9)
        # ['.', '.', '.', '.', '.', '.', '.', '.', '.']
        self.turn = 'X'

    def show_board(self):
        print(self.board)

    def set(self, row, col):
        pass

    def set_winner(self):
        # 가로 3줄
        # 세로 3줄



        pass

    def change_turn(self):
        pass


if __name__ == '__main__':
    game_engine = TictactoeGameEngine()
    game_engine.show_board()  # ...\n ...\n ...\n
    game_engine.set(2, 2)
    game_engine.show_board()  # ['.', '.', '.', '.', 'X', '.', '.', '.', '.']
    game_engine.set(2, 1)
    game_engine.set(2, 3)
    game_engine.show_board()  # ['.', '.', '.', 'X', 'X', 'X', '.', '.', '.']
    game_engine.board = ['.', '.', '.', 'X', 'X', 'X', '.', '.', '.']
    game_engine.set_winner()  # '-' - >'X'
    game_engine.change_turn()
    print(game_engine.turn)   # 'O'
    game_engine.change_turn()
    print(game_engine.turn)   # 'X'

    #
    # set_winner
    # self board
    # 이길수 있는 경우의 수 8개
