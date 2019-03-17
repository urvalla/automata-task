from grid import Grid
from grid_text_dumper import GridTextDumper
import unittest

class TestGrid(unittest.TestCase):
    def test_dump(self):
      grid = Grid()
      black_cells = [(-1, 0), (1, -1), (3, 1), (1, 1)]

      # prepare test grid
      for pos in black_cells:
          grid.toggle(*pos)

      dumper = GridTextDumper(grid)

      expected_dump = "\n".join(["00101", "10000", "00100"])
      self.assertEqual(dumper.dump(), expected_dump)


if __name__ == '__main__':
    unittest.main()
