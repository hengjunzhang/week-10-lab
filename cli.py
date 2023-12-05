from tictactoe import TicTacToe

def main():
    single_player = input("Single player mode? (y/n): ").lower() == 'y'
    game = TicTacToe(single_player)
    game.play_game()

if __name__ == '__main__':
    main()
