# dumps grid to text format
class GridTextDumper:
    WHITE_SYM = '0'
    BLACK_SYM = '1'

    def __init__(self, grid):
        self.grid = grid

    def dump(self):
        result = []
        dims = self.grid.get_dims()
        row_ending_x = dims[0][1]
        row = []

        for cell in self.grid.scan():
            x, y, is_white = cell
            row.append(self.WHITE_SYM if is_white else self.BLACK_SYM)
            if row_ending_x == x:
                result.append(''.join(row))
                row = []

        return "\n".join(result)


