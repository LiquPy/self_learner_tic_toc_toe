import numpy as np


class tic_toc_toe_game(object):
    """
    board: 3x3 matrix where 1 = x; 2 =o; 0 = otherwise
    """
    def __init__(self):
        self.board = np.full((3,3), 0)
        self.turn = np.random.randint(1, 3)
        self.game_finished = 0

    def switch_turn(self):
        if self.turn == 1:
            self.turn = 2
        else:
            self.turn = 1

    def generate_valid_moves(self):
        valid_moves_array = []
        for i in range(3):
            for j in range(3):
                if game.board[i,j] == 0:
                    valid_moves_array.append((i, j))
        print(valid_moves_array)

    
    def update(self, position):
        if self.game_finished == 0:
            if (self.board[position] != 0):
                raise ValueError('Invalid move')
            self.board[position] = self.turn
            self.switch_turn()
            print(self.board, self.turn)

    def check_status(self):
        # check for win along rows
        for i in range(3):
            if list(self.board[i, :]).count(1) == 3 or list(self.board[i, :]).count(2) == 3:
                self.game_finished = 1
                return "Won"
        # check for win along columns
        for i in range(3):
            if list(self.board[:, i]).count(1) == 3 or list(self.board[:, i]).count(2) == 3:
                self.game_finished = 1
                return "Won"
        # check for win along diagonals
        if list(np.diag(game.board)).count(1) == 3 or list(np.diag(game.board)).count(2) == 3:
            self.game_finished = 1
            return "Won"
        if list(np.diag(np.fliplr(game.board))).count(1) == 3 or list(np.diag(np.fliplr(game.board))).count(2) == 3:
            self.game_finished = 1
            return "Won"
        return 'in_progress'

        # Check for ties
        if 0 not in game.board:
            self.game_finished = 1
            return "Drawn"


if __name__  == '__main__':
    game = tic_toc_toe_game()
    print(game.board, game.turn)
    for i in range(0,40):
        try :
            game.update((np.random.randint(0, 3), np.random.randint(0, 3)))
            game.generate_valid_moves()
        except ValueError:
            pass
        status = game.check_status()
        print(status)
        if status != 'in_progress':
            break
