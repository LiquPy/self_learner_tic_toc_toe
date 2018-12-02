from tic_toc_toe import tic_toc_toe_game
game_status = ['You won !', "in progress", "It's a tie", 'You lost :( ']

game = tic_toc_toe_game(mode='vscomputer')

print('Your number is "2". Rock on!')
while game.game_finished == 0:
    print(game.board)
    x,y = str(input('Enter your move (separate with comma):')).replace(' ', '').split(',')
    game.play((int(x)-1, int(y)-1))
    if game.game_finished == 1:
        print(game_status[game.status])
        break
print(game.board)
