import time

class Board:
    board = [ '_', '_', '_', '_', '_', '_', '_', '_', '_' ]
    pieces = ['x', 'o']
    lines = {
        'top': [0, 1, 2],
        'mid': [3, 4, 5],
        'bot': [6, 7, 8],
        'left': [0, 3, 6],
        'center': [1, 4, 7],
        'right': [2, 5, 8],
        'd1': [0, 4, 8],
        'd2': [2, 4, 6]
        }
    win = []

    def draw_board(self):
        board = self.board
        draw = ''
        for i in range(3):
            for j in range(3):
                draw += ('|' + str((i * 3) + j + 1))
            draw += ('|\n')

        draw += '-------\n'

        for i in range(3):
            for j in range(3):
                draw += ('|' + board[i * 3 + j])
            draw += ('|\n')

        print(draw)

    def over(self):
        b = self.board
        wins = self.win_lines(b)
        for i in wins:
            c = set(wins.get(i))
            if len(c) == 1 and not(c.issuperset({'_'})):
               self.win = self.lines.get(i)
               self.print_win()
               return True
        else: 
            return False

    def win_lines(self, b):
        wins = {
                'top': [b[0], b[1], b[2]],
                'mid': [b[3], b[4], b[5]],
                'bot': [b[6], b[7], b[8]],
                'left': [b[0], b[3], b[6]],
                'center': [b[1], b[4], b[7]],
                'right': [b[2], b[5], b[8]],
                'd1': [b[0], b[4], b[8]],
                'd2': [b[2], b[4], b[6]]
                }
                
        return wins

    def print_win(self):
        for i in self.win:
            self.board[i] = '\u001b[31m' + self.board[i] + '\u001b[0m'

        self.draw_board()

    def place_piece(self, val, index):
        piece = self.pieces[index]
        if self.check_valid(val):
            self.board[val - 1] = piece

            return True
        else:
            return False

    def check_valid(self, val):
        if val > 9 or val < 1:
            return False
        elif self.board[val - 1] == '_':
            return True
        else:
            return False 
    
    def print_turn(self, turn):
        print(self.pieces[turn] + "'s turn")

class Game:
    board = Board()
    turn = 0

    def run(self):
        while not(self.board.over()):
            self.board.draw_board()

            self.board.print_turn(self.turn % 2)
            in_val = input('enter the tile you want to claim:')

            if self.is_exit(in_val):
                break
            
            if self.valid_input(in_val):
                in_val = int(in_val)
            else:
                print('please enter integers.')
                time.sleep(0.5)
                continue

            if self.board.place_piece(in_val, self.turn % 2):
                self.turn += 1
            else:
                print('please choose a valid square.')
                time.sleep(0.5)
                continue

    def valid_input(self, val):
        if val.isnumeric():
            return True
        else:
            return False

    def is_exit(self, val):
        if val == 'exit' or val == 'q' or val == 'quit':
            return True
        return False

new_game = Game()
new_game.run()
