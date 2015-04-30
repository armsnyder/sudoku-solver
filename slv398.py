#!/usr/bin/env python
# Author(s) names AND netid's: Michael Nowakowski (mjn912), Adam Snyder (ars123) and Steven Vorbrich (slv398)
# Date: 1 May 2015
#

import math
import copy


class SudokuBoard:
    """This will be the sudoku board game object your player will manipulate."""
  
    def __init__(self, size, board):
      """the constructor for the SudokuBoard"""
      self.BoardSize = size #the size of the board
      self.CurrentGameBoard= board #the current state of the game board

    def set_value(self, row, col, value):
        """This function will create a new sudoku board object with the input
        value placed on the GameBoard row and col are both zero-indexed"""

        #add the value to the appropriate position on the board
        self.CurrentGameBoard[row][col]=value
        #return a new board of the same size with the value added
        return SudokuBoard(self.BoardSize, self.CurrentGameBoard)
                                                                  
                                                                  
    def print_board(self):
        """Prints the current game board. Leaves unassigned spots blank."""
        div = int(math.sqrt(self.BoardSize))
        dash = ""
        space = ""
        line = "+"
        sep = "|"
        for i in range(div):
            dash += "----"
            space += "    "
        for i in range(div):
            line += dash + "+"
            sep += space + "|"
        for i in range(-1, self.BoardSize):
            if i != -1:
                print "|",
                for j in range(self.BoardSize):
                    if self.CurrentGameBoard[i][j] > 9:
                        print self.CurrentGameBoard[i][j],
                    elif self.CurrentGameBoard[i][j] > 0:
                        print "", self.CurrentGameBoard[i][j],
                    else:
                        print "  ",
                    if (j+1 != self.BoardSize):
                        if ((j+1)//div != j/div):
                            print "|",
                        else:
                            print "",
                    else:
                        print "|"
            if ((i+1)//div != i/div):
                print line
            else:
                print sep


def parse_file(filename):
    """Parses a sudoku text file into a BoardSize, and a 2d array which holds
    the value of each cell. Array elements holding a 0 are considered to be
    empty."""

    f = open(filename, 'r')
    BoardSize = int( f.readline())
    NumVals = int(f.readline())

    #initialize a blank board
    board= [ [ 0 for i in range(BoardSize) ] for j in range(BoardSize) ]

    #populate the board with initial values
    for i in range(NumVals):
        line = f.readline()
        chars = line.split()
        row = int(chars[0])
        col = int(chars[1])
        val = int(chars[2])
        board[row-1][col-1]=val
    
    return board


def is_complete(sudoku_board):
    """Takes in a sudoku board and tests to see if it has been filled in
    correctly."""
    BoardArray = sudoku_board.CurrentGameBoard
    size = len(BoardArray)
    subsquare = int(math.sqrt(size))

    #check each cell on the board for a 0, or if the value of the cell
    #is present elsewhere within the same row, column, or square
    for row in range(size):
        for col in range(size):
            if BoardArray[row][col]==0:
                return False
            for i in range(size):
                if ((BoardArray[row][i] == BoardArray[row][col]) and i != col):
                    return False
                if ((BoardArray[i][col] == BoardArray[row][col]) and i != row):
                    return False
            #determine which square the cell is in
            SquareRow = row // subsquare
            SquareCol = col // subsquare
            for i in range(subsquare):
                for j in range(subsquare):
                    if((BoardArray[SquareRow*subsquare+i][SquareCol*subsquare+j]
                            == BoardArray[row][col])
                        and (SquareRow*subsquare + i != row)
                        and (SquareCol*subsquare + j != col)):
                            return False
    return True


def init_board(file_name):
    """Creates a SudokuBoard object initialized with values from a text file"""
    board = parse_file(file_name)
    return SudokuBoard(len(board), board)


def solve(initial_board, forward_checking = False, MRV = False, MCV = False,
    LCV = False):
    """Takes an initial SudokuBoard and solves it using back tracking, and zero
    or more of the heuristics and constraint propagation methods (determined by
    arguments). Returns the resulting board solution. """
    print "Your code will solve the initial_board here!"
    print "Remember to return the final board (the SudokuBoard object)."
    print "I'm simply returning initial_board for demonstration purposes."
    init_domain(initial_board, forward_checking)
    return initial_board


def update_domain(board, row, col, value):
    """
    Performs forward-checking by updating the domain of each space in a board given the addition of a value to a
    particular space.
    """
    for a in range(board.BoardSize):
        try:
            board.CurrentGameBoard[row][a].remove(value)
        except ValueError:
            pass
        except AttributeError:
            pass

    for a in range(board.BoardSize):
        try:
            board.CurrentGameBoard[a][col].remove(value)
        except ValueError:
            pass
        except AttributeError:
            pass

    square_width = int(math.sqrt(board.BoardSize))

    for a in range(square_width*(row/square_width), square_width*(row/square_width)+square_width):
        for b in range(square_width*(col/square_width), square_width*(col/square_width)+square_width):
            try:
                board.CurrentGameBoard[a][b].remove(value)
            except ValueError:
                pass
            except AttributeError:
                pass
    return


def init_domain(board, forward_checking):
    """
    Takes an initial board and modifies its CurrentGameBoard field to work with our code by replacing unsolved spaces
    with full domains, optionally performing forward checking
    """
    initial_game_board = board.CurrentGameBoard
    board.CurrentGameBoard = [[list(range(1, board.BoardSize+1)) for row in range(board.BoardSize)]
                              for column in range(board.BoardSize)]

    for row in range(board.BoardSize):
        for column in range(board.BoardSize):
            cell_value = initial_game_board[row][column]
            if cell_value:
                board.CurrentGameBoard[row][column] = cell_value
                if isinstance(cell_value, int) and forward_checking:
                    update_domain(board, row, column, cell_value)


def backtrack(board, forward_checking=False, mrv=False, mcv=False, lcv=False):
    """
    Recursive depth-first-search algorithm
    """
    for row in range(board.BoardSize):
        for column in range(board.BoardSize):
            cell_value = board[row][column]
            if isinstance(cell_value, list):
                for option in cell_value:
                    new_board = copy.deepcopy(board)
                    new_board.CurrentGameBoard[row][column] = option
                    if is_board_valid(new_board):
                        board = backtrack(new_board, forward_checking, mrv, mcv, lcv)
    return board


def is_board_valid(board):
    """
    Returns True if board is consistent; False if it is not
    """
    pass


if __name__ == '__main__':
    solve(init_board('input_puzzles/easy/4_4.sudoku'))