import numpy as np
import random
from tic_toc_toe import tic_toc_toe_game
import pandas as pd

# note that there are 3**9=19683 states available for the board
batch_start = 1
batch_end = 101
total_training_games_per_batch = 2000

for b_n in range(batch_start, batch_end):
    # loops over batches and generate training data
    
    main_df = pd.DataFrame([])
    print('batch {}'.format(b_n))
    for j in range(0, total_training_games_per_batch):
        # loops over matches in each batch and dumps training dataset
        
        game = tic_toc_toe_game(ai_mode=random.choice(['none', 'naive'])) # you can add 'ML' mode in training too; after training it for the first time.
        board_state_array = []
        game_scores = []
        game_moves = []
        game_move_array = []
        for i in range(0,10):
            #print(valid_moves)
            #print(game.moves)
            #print(game.game_finished)

            # select next move at random
            new_move_tuple = random.choice(game.valid_moves)
            
            board_state = game.board.flatten().copy()

            computers_move = game.play(new_move_tuple)

            if not computers_move == None:
                game_moves.append([*computers_move])
                game_scores.append(0)
                board_state_array.append(board_state)
                game_move_array.append(game.moves)
            #print(board_state, new_move_tuple, game.status, game.moves)
            game.generate_valid_moves()
            #print(game.board)
            if game.game_finished == 1:
                break

        # data points are consisted of board state followed by the last move made by computer
        # as an improvement to the current model, human's last move can also be added as input
        df = pd.concat([pd.DataFrame(board_state_array), pd.DataFrame(game_moves)], axis=1)
        df['score'] = game_scores
        df['moves'] = game_move_array
        #print(game.status)
        if game.status == 0:
            game.status = 1
        game.status += 1

        # score function to generate labels
        df.score = (game.status)*(df.moves + 9 - max(df.moves))*2
        if game.status == 2:
            df.score = df.score*(-1)
            
        #status_dict = {2: 'Loss', 3: 'tie', 4: 'win'}
        #df['status'] = status_dict[game.status] # game status
        #df['match'] = j # match number
            
        df.drop('moves', axis=1, inplace=True)
        main_df = pd.concat([main_df, df], axis=0)
        #print(df)

    # normalize scores
    main_df.score = main_df.score/max(abs(min(main_df.score)), max(main_df.score))
    main_df.to_csv('training_datasets/training_data_{}.csv'.format(b_n), index= None, header=None)
