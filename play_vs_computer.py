from tic_toc_toe import tic_toc_toe_game
game_status = ['You won !', "in progress", "It's a tie", 'You lost :( ']

game = tic_toc_toe_game(mode='vscomputer', ai_mode='ML')

print("Do not use Python's indexing notation, address the board cells with numbers from 1 to 3.")
print("Your number is '2'. Let's see if you can beat our AI Rock on!")
while game.game_finished == 0:
    print(game.board)
    try:
        x,y = str(input('Enter your move (separate with comma):')).replace(' ', '').split(',')
        game.play((int(x)-1, int(y)-1))
        if game.game_finished == 1:
            print(game_status[game.status])
            break
    except ValueError:
        pass
print(game.board)
