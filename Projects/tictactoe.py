class Board:
    def __init__(self):
        self.board = [[1,2,3],[4,5,6],[7,8,9]]
    def draw(self):
        print(f"""
        ---------
        |{self.board[0][0]}||{self.board[0][1]}||{self.board[0][2]}|    
        |{self.board[1][0]}||{self.board[1][1]}||{self.board[1][2]}|    
        |{self.board[2][0]}||{self.board[2][1]}||{self.board[2][2]}|
        ---------
        """)
        return None

    def get_data(self, move, coordinates):
        if move == 'X' or move == 'O':
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
        else:
            print('That is not a valid move!')

        return None

    def is_win(self):
        for symbol in ['X', 'O']:
            for row in self.board:
                if all(cell == symbol for cell in row):
                    return True
            for col in range(3):
                column_values = [self.board[row][col] for row in range(3)]
                if all(cell == symbol for cell in column_values):
                    return True
            main_diagonal_values = [self.board[i][i] for i in range(3)]
            if all(cell == symbol for cell in main_diagonal_values):
                return True
            other_diagonal_values = [self.board[i][2 - i] for i in range(3)]
            if all(cell == symbol for cell in other_diagonal_values):
                return True
        return False

def main():
    validation = input('Welcome to Tic Tac Toe!,would you like to play? Y/N: ')
    if validation.upper() == 'Y':
        game = Board()
        while not game.is_win():
            game.draw()
            move = input('Enter your move and the coordinates of it!: ')
            if len(move.split()) == 2:
                move,coordinates = move.split()
                game.get_data(move,coordinates)
            else:
                print('Invalid move!')
                continue
        print('You won!')
        game.draw()
        main()
    else:
        print('Thanks for playing!')
main()
