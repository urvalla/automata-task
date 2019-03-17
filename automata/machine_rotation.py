class MachineRotation:
    TOP = 0
    RIGHT = 1
    BOTTOM = 2
    LEFT = 3
    MOVES = (
        (0, 1),
        (1, 0),
        (0, -1),
        (-1, 0),
    ) 

    def __init__(self):
        self.rotation = self.RIGHT

    def rotate_clockwise(self):
        if self.LEFT == self.rotation:
            self.rotation = self.TOP
        else:
            self.rotation+= 1

    def rotate_counter_clockwise(self):
        if self.TOP == self.rotation:
            self.rotation = self.LEFT
        else:
            self.rotation-= 1

    def forward_operator(self):
        return self.MOVES[self.rotation]