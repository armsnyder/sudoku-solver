import unittest
import slv398


class TestInitBoard(unittest.TestCase):

    def test_4x4(self):
        board_size = 4
        board_data = [[0 for i in range(board_size)] for j in range(board_size)]
        board = slv398.SudokuBoard(board_size, board_data)
        slv398.init_domain(board, False)
        self.assertEqual(
            [[[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]],
             [[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]],
             [[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]],
             [[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]]],
            board.CurrentGameBoard)

    def test_9x9(self):
        board_size = 9
        board_data = [[0 for i in range(board_size)] for j in range(board_size)]
        board = slv398.SudokuBoard(board_size, board_data)
        slv398.init_domain(board, False)
        self.assertEqual(
            [[[1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9]],
             [[1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9]],
             [[1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9]],
             [[1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9]],
             [[1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9]],
             [[1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9]],
             [[1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9]],
             [[1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9]],
             [[1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9]]],
            board.CurrentGameBoard)

    def test_no_forward_checking(self):
        board_size = 4
        board_data = [[0 for i in range(board_size)] for j in range(board_size)]
        board_data[0][0] = 1
        board = slv398.SudokuBoard(board_size, board_data)
        slv398.init_domain(board, False)
        self.assertEqual(
            [[1, [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]],
             [[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]],
             [[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]],
             [[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]]],
            board.CurrentGameBoard)

    def test_with_forward_checking(self):
        board_size = 4
        board_data = [[0 for i in range(board_size)] for j in range(board_size)]
        board_data[0][0] = 1
        board = slv398.SudokuBoard(board_size, board_data)
        slv398.init_domain(board, True)
        self.assertEqual(
            [[1, [2, 3, 4], [2, 3, 4], [2, 3, 4]],
             [[2, 3, 4], [2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]],
             [[2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]],
             [[2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]]],
            board.CurrentGameBoard)

    def test_impossible(self):
        board_size = 4
        board_data = [[0 for i in range(board_size)] for j in range(board_size)]
        board_data[0][0] = 1
        board_data[1][0] = 1
        board = slv398.SudokuBoard(board_size, board_data)
        slv398.init_domain(board, True)
        self.assertEqual(
            [[1, [2, 3, 4], [2, 3, 4], [2, 3, 4]],
             [1, [2, 3, 4], [2, 3, 4], [2, 3, 4]],
             [[2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]],
             [[2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]]],
            board.CurrentGameBoard)

    def test_solve_4x4(self):
        newboard = slv398.init_board("input_puzzles/easy/4_4.sudoku")
        slv398.init_domain(newboard, False)
        newboard.print_board()
        self.assertEqual(True, slv398.is_complete(slv398.solve(newboard)))
        pass

    def test_solve_9x9(self):
        newboard = slv398.init_board("input_puzzles/easy/9_9.sudoku")
        slv398.init_domain(newboard, False)
        newboard.print_board()
        self.assertEqual(True, slv398.is_complete(slv398.solve(newboard)))
        pass

    def test_board_valid(self):
        newboard = slv398.init_board("input_puzzles/easy/4_4.sudoku")
        slv398.init_domain(newboard, False)
        newboard.print_board()
        self.assertEqual(True, slv398.is_board_valid(newboard))

    def test_FC_solve_9x9(self):
        print "Hello"
        newboard = slv398.init_board("input_puzzles/easy/16_16.sudoku")
        slv398.init_domain(newboard, True)
        newboard.print_board()
        self.assertEqual(True, slv398.is_complete(slv398.solve(newboard)))
        pass