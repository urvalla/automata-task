from grid import Grid
import unittest

class TestGrid(unittest.TestCase):
    def test_toggle(self):
        self.assertEqual(Grid().is_white(1, 2), True)
        self.assertEqual(Grid().toggle(1, 2).is_white(1, 2), False)
        self.assertEqual(Grid().toggle(1, 2).toggle(1, 2).is_white(1, 2), True)

    def test_get_dims(self):
      grid = Grid()
      black_cells = [(1, 2), (-2, -3), (1, -2)]

      # prepare test grid
      for pos in black_cells:
          grid.toggle(*pos)

      self.assertEqual(grid.get_dims(), ((-2, 1), (-3, 2)))

    def test_scan(self):
      grid = Grid()
      black_cells = [(1, 2), (-2, -3), (1, -2)]

      # prepare test grid
      for pos in black_cells:
          grid.toggle(*pos)

      counter = 0
      for cell in grid.scan():
          is_white_expected = (cell[0], cell[1]) not in black_cells
          self.assertEqual(cell[2], is_white_expected)
          counter+= 1

      expected_cell_count = 4 * 6 # Dims 4x6: x=(-2, 1), y=(-3, 2)
      self.assertEqual(counter, expected_cell_count)

if __name__ == '__main__':
    unittest.main()