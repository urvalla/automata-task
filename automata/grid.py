class Grid:
    WHITE = 0
    BLACK = 1

    def __init__(self):
        self._x_size = (0, 0)
        self._y_size = (0, 0)
        self._grid = {}

    # toggle color at x, y
    def toggle(self, x, y):
        row = self._grid.get(y, {})
        color = row.get(x, self.WHITE)

        row[x] = self._toggle_color(color)
        self._grid[y] = row

        self._update_size(x, y)

        return self

    # get dimensions of grid as pair of tuples ((min x, max x), (min y, max y))
    def get_dims(self):
        return (self._x_size, self._y_size)

    # check if color at x, y is white
    def is_white(self, x, y):
        return self._get(x, y) == self.WHITE

    # iterates over rectangle from top-left and yielding (x, y, is_white) tuples
    def scan(self):
        dims_x, dims_y = self.get_dims()
        for y in range(dims_y[1], dims_y[0] - 1, -1):
            for x in range(dims_x[0], dims_x[1] + 1):
                yield (x, y, self.is_white(x, y))

    # get color code at x, y
    def _get(self, x, y):
        return self._grid.get(y, {}).get(x, self.WHITE)

    def _update_size(self, x, y):
        self._x_size = (min(self._x_size[0], x), max(self._x_size[1], x))
        self._y_size = (min(self._y_size[0], y), max(self._y_size[1], y))

    @classmethod
    def _toggle_color(cls, color):
        return cls.WHITE if color == cls.BLACK else cls.BLACK