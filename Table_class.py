from Ball_class import Ball


class Table:
    def __init__(self, height, base, balls: list[Ball]):
        self.height = height
        self.base = base
        self.balls = balls