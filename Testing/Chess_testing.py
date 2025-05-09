import unittest
from Two_player_chess import Rook, Board


class TestRook(unittest.TestCase):
    def setUp(self):
        self.board = Board()
        self.rook = Rook('white', (0, 0))
        self.board.grid[0][0] = self.rook

        # Clear the entire row and column for testing
        for i in range(8):
            self.board.grid[0][i] = None  # Clear horizontal path
            self.board.grid[i][0] = None  # Clear vertical path
        self.board.grid[0][0] = self.rook  # Put the rook back

    def test_rook_valid_move(self):
        valid_moves = self.rook.valid_moves(self.board)
        self.assertIn((4, 0), valid_moves)  # vertical move
        self.assertIn((0, 4), valid_moves)  # horizontal move

    def test_rook_invalid_move(self):
        valid_moves = self.rook.valid_moves(self.board)
        self.assertNotIn((3, 3), valid_moves)  # diagonal is invalid for rook


if __name__ == '__main__':
    unittest.main()
