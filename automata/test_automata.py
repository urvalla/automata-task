from automata import Automata
from grid import Grid
from machine_rotation import MachineRotation

import unittest

class TestAutomata(unittest.TestCase):
    CASES = (
        (1, Grid().toggle(0, 0)),
        (2, Grid().toggle(0, 0).toggle(0, -1)),
        (3, Grid().toggle(0, 0).toggle(0, -1).toggle(-1, -1)),
    )

    def test_against_first_steps(self):
        for case in self.CASES:
            steps, expected_grid = case

            with self.subTest(msg="with steps = n", n=steps):
                grid = self._get_grid_for_steps(steps)
                self.assertEqual(grid._grid, expected_grid._grid)

    @staticmethod
    def _get_grid_for_steps(steps):
        # init
        machine_rotation = MachineRotation()
        grid = Grid()
        automata = Automata(grid=grid, machine_rotation=machine_rotation)

        for i in range(steps):
            automata.step()

        return grid


if __name__ == '__main__':
    unittest.main()