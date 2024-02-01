winner = None
record = {'X': 0, 'O': 0, 'Draw': 0}
counter_of_moves = 0


def current_record(win=None):
    if win == 'X':
        record['X'] += 1
    elif win == 'O':
        record['O'] += 1
    else:
        record['Draw'] += 1
    for item, count in record.items():
        count = str(count)
        print(item + ' ' + '->' + ' ' + count, end=' | ')


class Board:
    def __init__(self):
        self.board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    def draw(self):
        print(f"""
        ---------
        |{self.board[0][0]}||{self.board[0][1]}||{self.board[0][2]}|    
        |{self.board[1][0]}||{self.board[1][1]}||{self.board[1][2]}|    
        |{self.board[2][0]}||{self.board[2][1]}||{self.board[2][2]}|
        ---------
        """)
        return None

    def get_data(self, coordinates):
        if counter_of_moves % 2 == 0:
            move = 'O'
        else:
            move = 'X'
        if coordinates.isdigit() and 1 <= int(coordinates) <= 9:
            coordinates = int(coordinates)
            if 1 <= coordinates <= 3:
                if coordinates in self.board[0]:
                    coordinates_index = self.board[0].index(coordinates)
                    self.board[0][coordinates_index] = move
                else:
                    print('That is not a valid coordinate!')
            elif 4 <= coordinates <= 6:
                if coordinates in self.board[1]:
                    coordinates_index = self.board[1].index(coordinates)
                    self.board[1][coordinates_index] = move
                else:
                    print('That is not a valid coordinate!')
            elif 7 <= coordinates <= 9:
                if coordinates in self.board[2]:
                    coordinates_index = self.board[2].index(coordinates)
                    self.board[2][coordinates_index] = move
                else:
                    print('That is not a valid coordinate!')
            else:
                print('That is not a valid coordinate!')

        return None

    def is_win(self):
        global winner
        for symbol in ['X', 'O']:
            for row in self.board:
                if all(cell == symbol for cell in row):
                    winner = symbol
                    return True
            for col in range(3):
                column_values = [self.board[row][col] for row in range(3)]
                if all(cell == symbol for cell in column_values):
                    winner = symbol
                    return True
            main_diagonal_values = [self.board[i][i] for i in range(3)]
            if all(cell == symbol for cell in main_diagonal_values):
                winner = symbol
                return True
            other_diagonal_values = [self.board[i][2 - i] for i in range(3)]
            if all(cell == symbol for cell in other_diagonal_values):
                winner = symbol
                return True
        return False

    def is_draw(self):
        global winner
        winner = None
        return not any(str(cell).isdigit() for row in self.board for cell in row)


def main(validation_message='Welcome to Tic Tac Toe!,would you like to play? Y/N: '):
    global counter_of_moves
    validation = input(validation_message)
    while validation not in ['y','Y','n','N']:
        print('Not a valid input!')
        validation = input(validation_message)
    if validation.upper() == 'Y':
        game = Board()
        while True:
            counter_of_moves += 1
            game.draw()
            if counter_of_moves % 2 == 0:
               print('O plays')
            else:
                print('X plays')
            move = input('Enter your move!: ')
            game.get_data(move)
            if game.is_win():
                print(winner + ' ' + 'wins!')
                game.draw()
                break
            elif game.is_draw():
                game.draw()
                print("It's a stalemate!")
                break
        current_record(winner)
        print()
        main('Would you like to play again? Y/N: ')
    else:
        print('See you next time!')


if __name__ == '__main__':
    main()
