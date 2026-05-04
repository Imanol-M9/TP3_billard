from Ball_class import Ball
import math
import csv
from interface import HAUTEUR, LONGEUR, BORDURE, RAYON


class Table:
    def __init__(self, height, base, balls: list[Ball]):
        self.height = height
        self.base = base
        self.balls = balls
    
    def step_and_write(self, filename="current_sim.csv"):
        fields = ["Time", "Position_White", "Speed_White"]
        rows = []
        time = 0

        with open(filename, "w", newline="") as file:
            while self.balls[0].collision_with_wall(self.base, self.height):
                rows.append((time, self.balls[0].position, self.balls[0].speed))
                self.balls[0].step(0.025)
                time += 1
            rows.append((time, self.balls[0].position, self.balls[0].speed))
            csvwriter = csv.writer(file)
            csvwriter.writerow(fields)
            csvwriter.writerows(rows)


white = Ball("White", [100,100], 0, 20 )
table = Table(122, 214, [white])

table.step_and_write()