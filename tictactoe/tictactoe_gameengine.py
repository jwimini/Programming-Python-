class TictactoeGameEngine:
    def __init__(self):
        self.board = list('.' * 9)
        # ['.', '.', '.', '.', '.', '.', '.', '.', '.']
        self.turn = 'X'
        self.SIZE = 3

    def show_board(self):
        # print('  '.join(self.board[0:3]))
        # print('  '.join(self.board[3:6]))
        # print('  '.join(self.board[6:9]))
        for i, v in enumerate(self.board):
            print(v + '  ', end='')
            if i % 3 == 2:
                print()

    def set(self, row, col):
        # self.board에 위치에다가  = self.turn
        # input -> 처리 -> output: row, col -> 처리 -> index
        # row, col -> index
        # self.board[(row * 3 - 3) + (col - 1)] = self.turn
        index = (row - 1) * 3 + (col - 1)
        self.board[index] = self.turn

    def position_to_index(self, row, col):
        return (row - 1) * 3 + (col - 1)

    def set_winner(self):
        # -줄
        for row in range(1, 3 + 1):
            if self.board[self.position_to_index(row, 1)] == self.board[self.position_to_index(row, 2)] == self.board[
                self.position_to_index(row, 3)] == self.turn:
                return self.turn
        # |줄
        for col in range(1, 3 + 1):
            if self.board[self.position_to_index(1, col)] == self.board[self.position_to_index(2, col)] == self.board[self.position_to_index(3, col)] == self.turn:
                return self.turn

        # /
        if self.board[self.position_to_index(1, 3)] == self.board[self.position_to_index(2, 2)] == self.board[
            self.position_to_index(3, 1)] == self.turn:
            return self.turn

        # \
        if self.board[self.position_to_index(1, 1)] == self.board[self.position_to_index(2, 2)] == self.board[
            self.position_to_index(3, 3)] == self.turn:
            return self.turn

        # 끝나는 경우 : 무승부(승자가 없는 상태로 놓을 자리가 없음), 승자 결정(승자가 있음)
        # if self.board[0] != '.' and self.board[1] != '.' and self.board[2] != '.' and \
        #         self.board[3] != '.' and self.board[4] != '.' and self.board[5] != '.' and \
        #         self.board[6] != '.' and self.board[7] != '.' and self.board[8] != '.':
        if not '.' in self.board:
            return 'd'  # draw

    def change_turn(self):
        # if self.turn == 'X':
        #     self.turn = 'O'
        # else:
        #     self.turn = 'X'
        self.turn = 'O' if self.turn == 'X' else 'X'


if __name__ == '__main__':
    game_engine = TictactoeGameEngine()
    game_engine.show_board()  # ...\n...\n...
    game_engine.set(2, 2)
    game_engine.show_board()  # ['.','.','.','.','X','.','.','.','.']
    game_engine.set(2, 1)
    game_engine.set(2, 3)
    game_engine.show_board()  # ['.','.','.','X','X','X','.','.','.']
    game_engine.board = ['.', '.', '.', 'X', 'X', 'X', '.', '.', '.']
    game_engine.set_winner()  # '-'  -> 'X'
    game_engine.change_turn()
    print(game_engine.turn)  # 'O'
    game_engine.change_turn()
    print(game_engine.turn)  # 'X'

    # set_winner
    # self board
    # 이길수 있는 경우의 수 8개
