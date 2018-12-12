import numpy as np
import random
import pickle

#load pickled ANN model
with open('pickled_model.pkl', 'rb') as file:  
    predictive_model = pickle.load(file)

class tic_toc_toe_game(object):
    """
    board: 3x3 matrix where 1 = x; 2 =o; 0 = otherwise

    """
    def __init__(self, mode='training', ai_mode='ML'):
        self.board = np.full((3,3), 0)
        if mode == 'training':
            self.turn = 2 # 1: computer, 2: human
        else:
            self.turn = 2
        self.game_finished = 0
        self.moves = 0 # number of moves played
        self.generate_valid_moves()
        self.status = 1 # 3: won, 2: drawn, 1: in progress, 0: lost
        self.ai_mode = ai_mode # 'ML': next computer move based on trained ML, otherwise: hard-coded 

    def switch_turn(self):
        # Switches turns
        if self.turn == 1:
            self.turn = 2
        else:
            self.turn = 1

    def generate_valid_moves(self):
        # Generates a list of all (possible) valid moves
        valid_moves_array = []
        for i in range(3):
            for j in range(3):
                if self.board[i,j] == 0:
                    valid_moves_array.append((i, j))

        self.valid_moves = valid_moves_array

    
    def update(self, position):
        # updates status of game including board state, switches turn, check for results, ...
        if self.game_finished == 0:
            if (self.board[position] != 0):
                raise ValueError('Invalid move')
    
            self.board[position] = self.turn
            self.moves += 1
            self.switch_turn()
            self.generate_valid_moves()
            self.update_status()

    def computer_smart_move(self):
        # hard-coded smart moves in order to generate training dataset

        for the_move in self.valid_moves:
        # loop over rows to find wining move
            temporary_board = self.board.copy()
            temporary_board[the_move] = 1
            for i in range(3):
                if list(temporary_board[i, :]).count(1) == 3:
                    return the_move

        for the_move in self.valid_moves:
        # loop over column to find wining move
            temporary_board = self.board.copy()
            temporary_board[the_move] = 1
            for i in range(3):
                if list(temporary_board[:,i]).count(1) == 3:
                    return the_move

        for the_move in self.valid_moves:
        # look at first diagonal to find wining move
            temporary_board = self.board.copy()
            temporary_board[the_move] = 1
            if list(np.diag(temporary_board)).count(1) == 3:
                return the_move

        for the_move in self.valid_moves:
        # look at second diagonal to find wining move
            temporary_board = self.board.copy()
            temporary_board[the_move] = 1            
            if list(np.diag(np.fliplr(temporary_board))).count(1) == 3:
                return the_move

        for the_move in self.valid_moves:
        # loop over rows to find blocking move
            temporary_board = self.board.copy()
            temporary_board[the_move] = 2
            for i in range(3):
                if list(temporary_board[i, :]).count(2) == 3:
                    return the_move

        for the_move in self.valid_moves:
        # loop over column to find blocking move
            temporary_board = self.board.copy()
            temporary_board[the_move] = 2
            for i in range(3):
                if list(temporary_board[:,i]).count(2) == 3:
                    return the_move

        for the_move in self.valid_moves:
        # look at first diagonal to find blocking move
            temporary_board = self.board.copy()
            temporary_board[the_move] = 2
            if list(np.diag(temporary_board)).count(2) == 3:
                return the_move

        for the_move in self.valid_moves:
        # look at second diagonal to find blocking move
            temporary_board = self.board.copy()
            temporary_board[the_move] = 2            
            if list(np.diag(np.fliplr(temporary_board))).count(2) == 3:
                return the_move

        # if not a wining or blocking move was available return a random move
        return random.choice(self.valid_moves)
    
    def play(self, position):
        # human moves followed by computer move
        self.update(position) # players move
        
        if self.game_finished == 1:
            return None

        # computer's next move
        if self.ai_mode == 'ML':
            # computer plays based on trained ML model
            moves_ranks = {}
            for move in self.valid_moves:
                create_input_array = np.array(list(self.board.flatten()) + list(move)).reshape(1,-1)
                moves_ranks[move] = predictive_model.predict(create_input_array)[0]
            argmax = max(iter(moves_ranks.keys()), key=(lambda key: moves_ranks[key]))
            #print(moves_ranks, argmax)
            #new_move_tuple = random.choice(self.valid_moves)
            self.update(argmax) # computer's move
            return argmax
        elif self.ai_mode == 'naive':
            # computer plays naive, chooses randomly from possible valid moves
            computers_move = random.choice(self.valid_moves)
            self.update(computers_move)
            return computers_move
        else:
            # computer plays based on hard-coded smart moves
            computers_move = self.computer_smart_move()
            self.update(computers_move)
            return computers_move
        
    def update_status(self):
        # checks for win/lose/tie/inprogress and updates
        
        # check for win along rows
        for i in range(3):
            if list(self.board[i, :]).count(1) == 3:
                self.game_finished = 1
                self.status = 3
            elif list(self.board[i, :]).count(2) == 3:
                self.game_finished = 1
                self.status = 0 
        # check for win along columns
        for i in range(3):
            if list(self.board[:, i]).count(1) == 3:
                self.game_finished = 1
                self.status = 3
            elif list(self.board[:, i]).count(2) == 3:
                self.game_finished = 1
                self.status = 0
        # check for win along diagonals
        if list(np.diag(self.board)).count(1) == 3:
            self.game_finished = 1
            self.status = 3
        elif list(np.diag(self.board)).count(2) == 3:
            self.game_finished = 1
            self.status = 0
        if list(np.diag(np.fliplr(self.board))).count(1) == 3:
            self.game_finished = 1
            self.status = 3
        elif list(np.diag(np.fliplr(self.board))).count(2) == 3:
            self.game_finished = 1
            self.status = 0
        
        # Check for ties
        if (np.count_nonzero(self.board) == 9) and (self.game_finished == 0):
            self.game_finished = 1
            self.status = 2
        elif self.game_finished == 0:
            self.status = 1
        #print(self.board, np.count_nonzero(self.board), self.status, self.game_finished)


##if __name__  == '__main__':
##    game = tic_toc_toe_game()
##    print(game.board, game.turn)
##    for i in range(0,40):
##        try :
##            game.update((np.random.randint(0, 3), np.random.randint(0, 3)))
##            game.generate_valid_moves()
##        except ValueError:
##            pass
##        status = game.update_status()
##        print(status)
##        if status != 'in_progress':
##            break
