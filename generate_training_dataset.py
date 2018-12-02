import numpy as np
import random
from tic_toc_toe import tic_toc_toe_game
import pandas as pd

total_training_games = 20000
main_df = pd.DataFrame([])

for j in range(0, total_training_games):

    game = tic_toc_toe_game()
    board_state_array = []
    game_scores = []
    game_moves = []
    game_move_array = []
    for i in range(0,10):
        #print(valid_moves)
        #print(game.moves)
        #print(game.game_finished)
        
        new_move_tuple = random.choice(game.valid_moves)
        
        board_state = game.board.flatten().copy()


        game.update(new_move_tuple)

        game_moves.append([*new_move_tuple])
        game_scores.append(0)
        board_state_array.append(board_state)
        game_move_array.append(game.moves)
        #print(board_state, new_move_tuple, game.status, game.moves)
        game.generate_valid_moves()

        if game.game_finished == 1:
            break

    df = pd.concat([pd.DataFrame(board_state_array), pd.DataFrame(game_moves)], axis=1)
    df['score'] = game_scores
    df['moves'] = game_move_array
    df.score = game.status*7.5 + df.moves + 70/max(df.moves)
    df.drop('moves', axis=1, inplace=True)
    main_df = pd.concat([main_df, df], axis=0)
    #print(df)

main_df.to_csv('training_data.csv', index= None, header=None)
