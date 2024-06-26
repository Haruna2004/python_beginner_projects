from player import HumanPlayer,RandomComputerPlayer,GeniusComputerPlayer
import time
class TickTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)] #we will use a single list to rep 3x3 board
        self.current_winner = None #keep track of the winner!

    def print_board(self):
        #This is just for the row
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')
    
    @staticmethod
    def print_board_num():
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')
    
    def available_moves(self):
        #return []
        return [i for i, spot in enumerate(self.board) if spot == ' ']
        # moves = []
        # for (i,spot) in enumerate(self.board):
        #     #['x','x','o'] --> (0,'x'),(1,'x'),(2,'o') return the 
        #     #index and the value of the boards as a sequence of tuple
        #     if spot == ' ':
        #         moves.append(i)
        # return moves

    def empty_squares(self):
        return ' ' in self.board
    def num_empty_squares(self):
        return self.board.count(' ') #since board is a list
    def make_move(self,square,letter):
        #if valid move, then make move (assign square to letter)
        #then return false if Invalid
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square,letter):
                self.current_winner = letter
            return True
        return False
    def winner(self,square,letter):
        #winner if 3 in a row anywhere.. we have to check all these
        #first lets check the rows
        row_ind = square // 3
        row = self.board[row_ind*3 : (row_ind + 1) * 3]
        if all([spot == letter for spot in row]):
            return True

        #check column
        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True
        
        #check diagonal
        #but only if the square is an even number(0,2,4,6,8)
        #these are the only possible squares
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0,4,8]]
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2,4,6]]
            if all([spot == letter for spot in diagonal2]):
                return True
            
        #if all these fails
        return False




def play(game,x_player,o_player,print_game=True):
    #return the winner for the game or none for a tie!
    if print_game:
        game.print_board_num()

    letter = 'X' #starting letter
    #iterate while the game still has empty space
    #we don't have to worry about the winner because we will just return that 
    #which breaks the loop
    while game.empty_squares():
        #get move from the appropriate player
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)
        
        #lets define a function to make a move!
        if game.make_move(square,letter):
            if print_game:
                print(letter + f' makes a move to {square}')
                game.print_board()
                print('') #just empty line
            if game.current_winner:
                if print_game:
                    print(letter + ' wins!')
                return letter

            #after we made our move we need to alternater letters
            letter = 'O' if letter == 'X' else 'X' #swiches player
        #tiny break
        time.sleep(0.8)

    if print_game:
        print("It's a tie!")

if __name__ == '__main__':
    x_player = GeniusComputerPlayer('X')
    o_player = HumanPlayer('O')
    t = TickTacToe()
    play(t,x_player,o_player,print_game=True)



            
            
