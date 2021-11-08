import tkinter
from tkinter import messagebox

from tictactoe_gameengine import TictactoeGameEngine


class TictactoeGUI:
    def __init__(self):
        self.game_engine = TictactoeGameEngine()
        self.init_GUI()

    def init_GUI(self):
        self.CANVERS_SIZE = 300  # 캔버스 사이즈
        self.root = tkinter.Tk()
        self.root.title('틱택토')
        self.root.geometry(f'{self.CANVERS_SIZE}x{self.CANVERS_SIZE}')
        self.root.resizable(width=False, height=False)

        self.cavas = tkinter.Canvas(self.root, bg='white', width=self.CANVERS_SIZE, height=self.CANVERS_SIZE)

        self.cavas.pack()

        self.images = {}    # {'X': PhotoImage객체, 'O' PhotoImage 객체}
        self.images['X'] = tkinter.PhotoImage(file='X.gif')
        self.images['O'] = tkinter.PhotoImage(file='O.gif')

        self.cavas.bind('<Button-1>', self.click_handler)  # self.click_handler 괄호 쓰지 않기

        self.root.mainloop()

    def click_handler(self, event):
        row, col = self.coordinate_to_position(event.x, event.y)
        # set row, col
        self.game_engine.set(row, col)
        # show board
        self.game_engine.show_board()
        # set winner
        winner = self.game_engine.set_winner()
        # 승자가 있거나 무승부이면, 게임오버, 결과 표시
        if winner == 'O' or winner == 'X':
            messagebox.showinfo('GameOver', f'{winner} 이김~😝😝')
            self.root.quit()
        elif winner == 'd':
            messagebox.showinfo('GameOver', '무승부😙😙😙')
            self.root.quit()
        # change
        self.game_engine.change_turn()
        print('========')

    def draw_board(self):
        pass

    def coordinate_to_position(self, x, y):
        # row
        row = y // (self.CANVERS_SIZE // self.game_engine.SIZE) + 1
        # col
        col = x // (self.CANVERS_SIZE // self.game_engine.SIZE) + 1

        return row, col


if __name__ == '__main__':
    ttt_GUI = TictactoeGUI()
