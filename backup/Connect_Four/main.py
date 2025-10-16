from game_board import ConnectFourBoard

if __name__ == '__main__':
    # postive test1
    game = ConnectFourBoard()
    game.place_move(0, 0, 0)
    game.place_move(1, 4, 0)
    game.place_move(0, 0, 2)
    game.place_move(1, 2, 2)
    game.place_move(0, 0, 3)
    game.place_move(1, 4, 4)
    game.place_move(0, 0, 4)
    game.place_move(1, 2, 3)
    game.place_move(0, 0, 5)

    # postive test2
    game = ConnectFourBoard()
    game.place_move(0, 4, 0)
    game.place_move(1, 0, 3)
    game.place_move(0, 3, 1)
    game.place_move(1, 1, 4)
    game.place_move(0, 2, 2)
    game.place_move(1, 2, 5)
    game.place_move(0, 0, 4)
    game.place_move(1, 3, 6)


