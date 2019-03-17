class Automata:
    def __init__(self, grid, machine_rotation):
        self.machine_rotation = machine_rotation
        self.grid = grid
        self.pos_x = 0
        self.pos_y = 0

    def step(self):
        if self.grid.is_white(self.pos_x, self.pos_y):
            self.machine_rotation.rotate_clockwise()
            dx, dy = self.machine_rotation.forward_operator()
        else:
            self.machine_rotation.rotate_counter_clockwise()
            dx, dy = self.machine_rotation.forward_operator()

        self.grid.toggle(self.pos_x, self.pos_y)
        self.pos_x = self.pos_x + dx
        self.pos_y = self.pos_y + dy
