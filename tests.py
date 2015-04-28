import unittest
import slv398


class TestInitBoard(unittest.TestCase):

    def test_4x4(self):
        board_size = 4
        board_data = [[0 for i in range(board_size)] for j in range(board_size)]
        board = slv398.SudokuBoard(board_size, board_data)
        self.assertEqual(
            [[[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]],
             [[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]],
             [[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]],
             [[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]]],
            slv398.init_domain(board))